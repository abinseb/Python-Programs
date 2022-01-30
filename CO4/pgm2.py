class bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposite(self,amount):
        self.bal=self.bal+amount
        print("amount deposited succesfully")
        return self.bal
    def withdrawel(self,amount):
        if amount>self.bal:
            print("insufficient balance withdrawel is not possible")
        else:
            self.bal=self.bal-amount
            print("withdrawel is succesfull")
        return self.bal
a=bank("1001","Niranjan","saving",3000)
damount=float(input("Enter the amount to be deposite:"))
print("amount balance:",a.deposite(damount))
wamount=float(input("Enter the amount to be withdraw:"))
print("Amount balance aftre withdraw:",a.withdrawel(wamount))