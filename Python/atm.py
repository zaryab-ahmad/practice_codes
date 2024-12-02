
import os

class ATM:
    
    
    def __init__(self,name,ID,balance):
        self.name=name
        self.ID=ID
        self.balance=balance
        
    def newATM(self,name,ID,balance):
        self.name=name
        self.ID=ID
        self.balance=balance
    def transiction(self,amount):
        return self.balance - self.amount
    def deposte(self,amount):
        return self.balance + self.amount
    def __str__(self):
        return f"Card Holder {self.name} the total amount in card is: {self.balance} and ID: {self.ID}"

a1 = ATM("khan",3456,4009)
i=0
newAtm = 0
while i==0:
    newAtm = int(input("For to apply New ATM card Enter 1: "))
    continue
    if newAtm == 1:
        name = input("Enter your Good name sir: ")
        numbers = [1,2,3,4,5,6,7,8,9,0]
        ID = random.randint(numbers,4)
        amount = int(input("Enter the Amount you want to load in Card:"))
        print(name,ID,amount)
        a = ATM(name,ID,amount)
    i= int(input("if you want to create a new account enter 0 else 1: "))
    
    
    
    
    
    
    
    
    
    
    
        

