class ATMMachine:
    def __init__(self, pin):
        self.balance = 1000  # Initial balance
        self.pin = pin       # User's initial PIN
        self.transaction_history = []  # To store all transactions

    # Function to verify the PIN
    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN verified successfully.")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("Your account is locked due to too many failed attempts.")
        return False

    # Function for balance inquiry
    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append(f"Balance inquiry: ${self.balance}")

    # Function for cash deposit
    def deposit_cash(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Deposit must be greater than 0.")
            else:
                self.balance += amount
                print(f"${amount} deposited successfully.")
                self.transaction_history.append(f"Deposited: ${amount}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Function for cash withdrawal
    def withdraw_cash(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Withdrawal must be greater than 0.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"${amount} withdrawn successfully.")
                self.transaction_history.append(f"Withdrawn: ${amount}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Function to change the PIN
    def change_pin(self):
        current_pin = input("Enter your current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN changed")
            else:
                print("New PINs do not match.")
        else:
            print("Current PIN is incorrect.")

    # Function to display transaction history
    def display_transaction_history(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

# Main function to simulate the ATM machine
def main():
    atm = ATMMachine(pin="1234")  # Initialize ATM with default PIN
    print("Welcome to the ATM Machine!")
    
    if atm.verify_pin():
        while True:
            print("\nSelect an option:")
            print("1. Balance Inquiry")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                atm.balance_inquiry()
            elif choice == "2":
                amount = input("Enter the amount to deposit: ")
                atm.deposit_cash(amount)
            elif choice == "3":
                amount = input("Enter the amount to withdraw: ")
                atm.withdraw_cash(amount)
            elif choice == "4":
                atm.change_pin()
            elif choice == "5":
                atm.display_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
