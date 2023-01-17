from acc.new_acc import CreateAccount


new_account = CreateAccount(1234, 996688, 1000, "Henrico Nardelli", "111.222.333-44")
new_account.consult_balance()
new_account.deposit(1000)
new_account.consult_balance()

print("-"*30)

new_account2 = CreateAccount(4321, 886655, 10000, "Stuart Lirou", "222.555.666-99")
new_account2.consult_balance()
new_account2.switch(5000, new_account)
new_account2.consult_balance()

print("-"*30)

new_account.limit = 1500
print(f"Limit ${new_account.limit:.2f}")
new_account2.limit = 12000
print(f"Limit ${new_account2.limit:.2f}")

print("-"*30)

new_account.consult_balance()
new_account2.consult_balance()
new_account.withdraw(8200)
new_account2.withdraw(6000)
new_account.deposit(12000)
new_account.consult_balance()
new_account2.deposit(12000)
new_account2.consult_balance()