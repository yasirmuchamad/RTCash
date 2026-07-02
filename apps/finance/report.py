from .models import FundBalance

def get_cash_report():
    balances = FundBalance.objects.all()
    total_balance = sum(
        item.balance 
        for item in balances
        )
    return {
        "initial_balance": 0,
        "income": 0,
        "expense": 0,
        "final_balance": total_balance,
    }