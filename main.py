class User:
    def __init__(self):
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self
        
    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        return self


felix = User()
jess = User()
elijah = User()

felix.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

jess.make_deposit(300).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

elijah.make_deposit(200).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

felix.transfer_money(10000,elijah)
elijah.display_user_balance()
felix.display_user_balance()


