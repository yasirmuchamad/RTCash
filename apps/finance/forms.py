from django import forms
from .models import ContributionPackage, ContributionPeriod
from apps.residents.models import Resident

class PaymentForm(forms.Form):
    resident = forms.ModelChoiceField(queryset=Resident.objects.all(), label='Warga')
    package = forms.ModelChoiceField(queryset=ContributionPackage.objects.all(), label='Paket Iuran')
    period = forms.ModelChoiceField(queryset=ContributionPeriod.objects.all(), label='Periode Iuran')