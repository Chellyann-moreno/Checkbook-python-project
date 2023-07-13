import datetime

def current_balance():
    with open('checkbook_history.txt') as f:
        bal = int(f.read())
    print("Available Balance is:", bal)

def deposit(balance):
    amount = int(input("How much would you like to deposit? "))
    balance += amount
    with open('checkbook_history.txt', 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Deposit\t{timestamp}\t{amount}\n")
    return balance

def withdrawal(balance):
    amount = int(input("How much would you like to withdraw? "))
    if amount <= balance:
        balance -= amount
        with open('checkbook_history.txt', 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Withdrawal\t{timestamp}\t{amount}\n")
    else:
        print("Insufficient balance.")
    return balance

def view_transactions():
    with open('checkbook_history.txt') as f:
        transactions = f.readlines()
    for transaction in transactions:
        print(transaction.strip())

def view_transactions_by_category(category):
    with open('checkbook_history.txt') as f:
        transactions = f.readlines()
    for transaction in transactions:
        details = transaction.strip().split('\t')
        if details[0].lower() == category.lower():
            print(transaction.strip())

def search_transactions(keyword):
    with open('checkbook_history.txt') as f:
        transactions = f.readlines()
    for transaction in transactions:
        if keyword.lower() in transaction.lower():
            print(transaction.strip())

def modify_transaction():
    # Provide the implementation to modify a past transaction
    pass

def main():
    print("~~~~~~~~~ HELLO, WELCOME BACK! ~~~~~~~~~")
    
    while True:
        print("Please select an option:")
        print("1. View Current Balance")
        print("2. Make a Withdrawal")
        print("3. Make a Deposit")
        print("4. View All Transactions")
        print("5. View Transactions by Category")
        print("6. Search Transactions")
        print("7. Modify a Past Transaction")
        print("8. Exit")
        choice = input("Choice? ")
        print()

        if choice == "1":
            current_balance()
            print()
        
        elif choice == "2":
            bal = withdrawal(bal)
            current_balance()
            print()

        elif choice == "3":
            bal = deposit(bal)
            current_balance()
            print()

        elif choice == "4":
            view_transactions()
            print()

        elif choice == "5":
            category = input("Enter a category: ")
            view_transactions_by_category(category)
            print()

        elif choice == "6":
            keyword = input("Enter a keyword: ")
            search_transactions(keyword)
            print()

        elif choice == "7":
            modify_transaction()
            print()

        elif choice == "8":
            print("THANK YOU, HAVE A GREAT DAY!")
            with open('checkbook_history.txt', 'w') as f:
                f.write(str(bal))
            break

        else:
            print("PLEASE SELECT OPTIONS 1 THROUGH 8")
            print()

if __name__ == '__main__':
    main()
