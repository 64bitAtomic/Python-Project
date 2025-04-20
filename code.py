import datetime

ledger = []

def add_transaction(type_, amount, description):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    balance = ledger[-1]['balance'] if ledger else 0
    if type_ == 'Income':
        balance += amount
    elif type_ == 'Expense':
        balance -= amount

    transaction = {
        'date': date,
        'type': type_,
        'amount': amount,
        'description': description,
        'balance': balance
    }
    ledger.append(transaction)
    print(f"{type_} added successfully!")

def view_ledger():
    print("\n--- Ledger ---")
    for entry in ledger:
        print(f"{entry['date']} | {entry['type']} | {entry['amount']} | {entry['description']} | Balance: {entry['balance']}")
    print("----------------")

def get_balance():
    balance = ledger[-1]['balance'] if ledger else 0
    print(f"\nCurrent Balance: ₹{balance}\n")

# Simple menu-driven interface
while True:
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Ledger")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter income amount: ₹"))
        desc = input("Enter description: ")
        add_transaction('Income', amount, desc)

    elif choice == '2':
        amount = float(input("Enter expense amount: ₹"))
        desc = input("Enter description: ")
        add_transaction('Expense', amount, desc)

    elif choice == '3':
        view_ledger()

    elif choice == '4':
        get_balance()

    elif choice == '5':
        print("Exiting the Ledger Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Pleas e try again.") # type: ignore