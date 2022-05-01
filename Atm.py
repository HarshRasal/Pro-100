import os 
import shutil

class Atm():
    def _init_(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        
        def balance_enquiry(self):
            print("your balance is 50000")

        def cashwidrawal(self,amount):
            newamount = 50000-amount
            print (" you have widrawn amount "+str(amount)+". your remaining balance is"+str(newamount))

def main():
    card_number = input ("insert your card number")
    pin_number  = input ("insert your pinnumber")
    

    new_user = Atm(card_number,pin_number)
    print("choose your activity")
    print("1.BalanceEnquiry 2.widrawal")
    activity =int( input(" please enter activivty number"))
    if (activity == 1):
        new_user.balance_enquiry()
    elif (activity == 2):
        amount = int(input("please enter the amount of widrawal"))
        new_user.cashwidrawal()
    else:
        print ("please enter a valid number")

if __name__ == "__main__":
    main()