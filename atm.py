class Bank:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 500000")

    def withdrawl_amount(self,amount):
        balance_amount = 500000 - amount
        print("Your withdrawled amount "+str(amount) +". Your remaining balance is "+ str(balance_amount))


def processing():
    name = input("Enter your Name : ")
    print("Hi "+str(name)+" enter the Following ")
    card_number = input("Enter your card number :-) ")
    pin_number  = input("Enter your pin number :-) ")

    user1 =  Bank(card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("enter activity number (1 or 2):- "))

    if (activity == 1):
        user1.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount to be Withdrawled :-) "))
        user1.withdrawl_amount(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    processing()
