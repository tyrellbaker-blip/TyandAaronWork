class bank_account:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("Enter the amount you would like to "
                             "deposit: "))
        self.balance += amount
        print(f"Thank you for depositing, your deposit amount was "
              f"${amount}.")

    #TODO: Implement the withdrawal and display functions. Withdrawal should
    # first ask the user how much money they want to withdraw and then
    # withdraw it from their balance.

    #TODO: Implement the display function, which prints the balance for the
    # user.


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
