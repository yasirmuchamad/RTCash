from django.db import transaction
from .models import (
    PackageItem, 
    Payment, 
    PaymentDetail, 
    FundBalance
)
from apps.audit.models import AuditLog
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@transaction.atomic
def create_payment(resident, package, period):
    package_items = PackageItem.objects.filter(package=package).select_related('contribution')
    total = 0
    payment = Payment.objects.create(resident=resident, package=package, period=period, total_amount=0)

    for item in package_items:
        contribution = item.contribution
        ammount = contribution.default_amount
        PaymentDetail.objects.create(payment=payment, contribution=contribution, amount=ammount)
        fund = FundBalance.objects.get(fund_type=contribution.destination)
        fund.balance += ammount
        fund.save() 
        total += ammount

    payment.total_amount = total
    payment.save()
    AuditLog.objects.create(
        user=resident.user,
        action="CREATE_PAYMENT",
        model="Payment",
        object_id=payment.id,
        description=(
            f"{resident} "
            f"membayar "
            f"{package}"
            )
    )
    

    print("Akan kirim event")

    channel_layer = get_channel_layer()
    balances = FundBalance.objects.all()
    data = {}

    for item in balances:
        data[item.fund_type] = float(item.balance)

    print(data)
        
    async_to_sync(
        channel_layer.group_send
        )(
            "balance_room",
            {
                "type": "balance_update",
                "balances": data
            }
    )
    print("Event terkirim")

    return payment