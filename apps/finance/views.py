from django.shortcuts import render, redirect
from .forms import PaymentForm
from .services import create_payment as process_payment
from .models import Payment
from .utils import payment_status
from apps.residents.models import Resident
from .models import ContributionPeriod, FundBalance

# Create your views here.
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            process_payment(
                resident=form.cleaned_data['resident'],
                package=form.cleaned_data['package'],
                period=form.cleaned_data['period']
            )
            return redirect('finance:payment_list')  # Redirect to a success page
    else:
        form = PaymentForm()
    
    return render(request, 'finance/payment_form.html', {'form': form})

def payment_list(request):
    # This view will list all payments, you can customize it as needed
    payments = Payment.objects.select_related('resident', 'package', 'period').all()
    return render(request, 'finance/payment_list.html', {'payments': payments}) 

def resident_payment_status(request):
    residents = Resident.objects.all()
    period = ContributionPeriod.objects.filter(is_active=True).first()  # Assuming you want to check for the active period 
    data = []
    for resident in residents:
        status = payment_status(resident, period)
        data.append({'resident': resident, 'status': status})
    return render(request, 'finance/payment_status.html', {'data': data, 'period': period})

def dashboard(request):
    balance = FundBalance.objects.all()
    return render(request, 'finance/dashboard.html', {'balance': balance})