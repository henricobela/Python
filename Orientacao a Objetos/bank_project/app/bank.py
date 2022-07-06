from acc.new_acc import CreateAccount


new_account = CreateAccount(1234, 996688, 1000, "Henrico Nardelli", "111.222.333-44")
print(f"Balance: ${new_account.consult_balance():.2f}")
new_account.deposit(1000)
print(f"Balance: ${new_account.consult_balance():.2f}")
