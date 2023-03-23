bal=126000

def current_balance(bal):
    print("Available Balance is:",bal)
def Deposit(amount,bal):
    return(bal+amount)
    current_balance()

def Withdrawal(amount,bal):
    return (bal-amount)
    current_balance()

with open('checkbook_history.txt') as f:
            bal=f.read()
            bal=int(bal)
print(" ~~~~~~~~~ HELLO, WELCOME BACK! ~~~~~~~~~")
while True:
    print("Please Select an option:")
    print("                        ")
    print("1. View Current Balance")
    print("2. Make a Withdrawal")
    print("3. Make a Deposit")
    print("4. Exit")
    choice=input("Choice?")
    
    if choice =="1":
        current_balance(bal)
        
    elif choice== "2":
        
        amount=int(input("How much would you like to withdraw?"))
        bal=Withdrawal(amount,bal)
        current_balance(bal)
    elif choice=="3":
        
        amount=int(input("How much would you like to deposit?"))
        bal=Deposit(amount,bal)
        Deposit(amount,bal)
        current_balance(bal)
    elif choice=="4":
        
        print("THANK YOU, HAVE A GREAT DAY!")
        with open('checkbook_history.txt', 'w') as f:
            f.write(str(bal))
        break
    else: 
        print("PLEASE SELECT OPTIONS 1 THROUGH 4")
        print("                       ") 