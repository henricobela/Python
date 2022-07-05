from account import account
from transactions import transactions


new_account = account.CreateAccount(1234, 996688, 1000,"Henrico Nardelli", "111.222.333-44")

print(f"Balance: ${new_account.consult_balance():.2f}")

