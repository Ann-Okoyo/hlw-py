class Bank:
    balance =0
    def __init__(self, name,number,branch):
        self.account_name = name
        self.account_number = number
        self.account_branch = branch
    def deposit(self, amt):
        self.balance+=amt
        return f"You have withdrawn {amt}. Your new balance is {self.balance} ksh"
    def withdraw(self, amt):
        self.balance-=amt
        return f"You have withdrawn ksh{amt}. Your new balance is {self.balance}"
    def status(self):
        if self.balance==0:
            return f"Your account is dormant"
        else:
            return f"Your bank account is active"






    