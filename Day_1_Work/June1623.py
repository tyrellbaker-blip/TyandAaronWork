class bank_account:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("Enter the amount you would like to "
                             "deposit: "))
        self.balance += amount
        print(f"Thank you for depositing, your deposit amount was "
              f"${amount}.")


def main():
    # This is a comment, has no impact on our code
    """
    Variables are like little boxes in your computer's memory that reference
    specific information.
    """
    my_bank_account = bank_account()
    my_bank_account.deposit()


if __name__ == '__main__':
    main()
