class atm:
    def __init__ (self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkbalance(self):
        print("your balance is 15,000")
    def withdrawel(self,amount):
        newamount=15000-amount
        print("you have withdrawn amount:- "+str(amount)+"your new balance is "+str(newamount))
def main():
    cardnumber=input("insert your cardnumber")
    pinnumber=input("enter pin")
    newUser=atm(cardnumber,pinnumber)
    print("choose your activity")
    print("1. balanceinquirey  2.withdraw")
    activity=int(input("enter activity number"))
    if(activity==1):
        newUser.checkbalance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        newUser.withdrawel(amount)
    else:
        print("enter a valid number")
if __name__=="__main__":
    main()
    