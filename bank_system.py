class User():
    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
    def __userinfo__(self):
        print("Personal Information")
        print("Name :",self.name)
        print("Surname :",self.surname)
        print("Age :",self.age)
        print("Gender :",self.gender)

class Bank(User):
    def __init__(self,name,surname,age,gender):
        super().__init__(name,surname,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Balance has been update : $",self.balance)
    
    def withdrawal(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("not enought money")
        else:
            self.balance = self.balance - self.amount
            print("Done!")

Vahan = Bank("Vahan","Mkrtchyan",21,"Male")
Bank.__userinfo__(Vahan)
Vahan.deposit(200)
Vahan.withdrawal(200)
