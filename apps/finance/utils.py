from .models import Payment

def payment_status(resident, period):
    paid = Payment.objects.filter(resident=resident, period=period).exists()
    
    if paid:
        return 'Lunas'
    
    return 'Lunas' if paid else 'Belum Lunas'