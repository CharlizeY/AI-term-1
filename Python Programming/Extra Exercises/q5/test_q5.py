from q5 import CashAccount


def test_simulation():
    initial_balance = 1000.0
    print(f"Creating a new cash account in October with an initial balance of £{initial_balance}.")
    account = CashAccount(initial_balance)
    
    print("User makes 10 deposits of £10 each in October...")
    for i in range(10):
        account.deposit(10.0)
    print(f"Balance after the 10 deposits: £{account.balance}")
    assert account.balance == 1100.0

    print("User makes 10 withdrawals of £100 each in October...")
    for i in range(10):
        account.withdraw(100.0)
    print(f"Balance after the 10 withdrawals: £{account.balance}")
    assert account.balance == 100.0
    print(account.withdrawl_count)
    
    print("The bank deducts its service fee at the end of October")
    account.deduct_monthly_fees()
    print(f"Balance after deduction: £{account.balance}")
    assert account.balance == 94.0

    account.deduct_monthly_fees()  # should not deduct any fee.
    print(f"Starting balance in November: £{account.balance}")
    assert account.balance == 94.0


if __name__ == "__main__":
    test_simulation()
