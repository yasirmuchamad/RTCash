from django.contrib import admin
from .models import (
        ContributionType, 
        ContributionPackage, 
        PackageItem, 
        Payment, 
        PaymentDetail, 
        FundBalance
)

# Register your models here.
@admin.register(ContributionType)
class ContributionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'default_amount')
    search_fields = ('name',)   

@admin.register(ContributionPackage)
class ContributionPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(PackageItem)
class PackageItemAdmin(admin.ModelAdmin):    
    list_display = ('package', 'contribution')
    list_filter = ('package',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('resident', 'package', 'total_amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('resident__name',)

@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ('payment', 'contribution', 'amount')

@admin.register(FundBalance)
class FundBalanceAdmin(admin.ModelAdmin):
    list_display = ('fund_type', 'balance')
    list_filter = ('fund_type',)