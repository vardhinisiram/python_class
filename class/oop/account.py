class account:
    def __init__(self,name,num,amount) -> None:
        self.name=name
        self.accnum=num
        self.amount=amount
    

    def get_details(self):
        print(self.name,self.accnum,self.amount)
    def get_balance(self):
        print(self.amount)
    def withdrawl(self,withdrawl):
        self.amount=self.amount-withdrawl
        print(self.amount)

acc1=account("usha",10115214,5000)
acc2=account("priya",10115215,6000)
acc1.get_balance()
acc1.withdrawl(2000)
acc2.get_details()