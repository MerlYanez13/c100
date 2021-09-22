class atm(object):
    def __init__(self,cardno,pin): 
        self.cardno=cardno
        self.pin=pin
    def checkballance(self):
        print("Your Balance Is $150")
    def withdrawl(self,amount):
        Balance=150-amount
        print("Your Balance is: ", Balance)

audi=atm(12341234, 1010)
audi.checkballance()
audi.withdrawl(20)