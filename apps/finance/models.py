from django.db import models
from apps.residents.models import Resident

# Create your models here.
class ContributionType(models.Model):
    DESTINATION = (
        ('main_cash', 'Kas RT'),
        ('social_cash', 'Kas Sosial'),
        ('owner_cash', 'Uang Meja'),
    )
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=20, choices=DESTINATION)
    default_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ContributionPackage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PackageItem(models.Model):
    package = models.ForeignKey(ContributionPackage, on_delete=models.CASCADE, related_name='items')
    contribution = models.ForeignKey(ContributionType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.package.name} - {self.contribution.name}"

class ContributionPeriod(models.Model):
    TYPE = (
        ('weekly', 'Mingguan'),
        ('monthly', 'Bulanan'),
        ('quarterly', 'Triwulanan'),
        ('yearly', 'Tahunan'),
    )
    name = models.CharField(max_length=100)
    period_type = models.CharField(max_length=20, choices=TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    package = models.ForeignKey(ContributionPackage, on_delete=models.PROTECT)
    period = models.ForeignKey(ContributionPeriod, on_delete=models.PROTECT, null=True, blank=True)
    total_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'resident', 
                    'package',
                    'period'], name='unique_payment_per_period')
        ]

    def __str__(self):
        return f"{self.resident} - {self.package} - {self.period}"

class PaymentDetail(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='details')
    contribution = models.ForeignKey(ContributionType, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.contribution.name}"

class FundBalance(models.Model):
    TYPE = (
        ('main_cash', 'Kas RT'),
        ('social_cash', 'Kas Sosial'),
        ('owner_cash', 'Uang Meja'),
    )
    fund_type = models.CharField(max_length=20, choices=TYPE, unique=True)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_fund_type_display()

