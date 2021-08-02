class User:
    def __init__(self):
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
    
    def make_withdrawal(self,amount):
        self.balance -= amount

    def display_user_balance(self):
        print(self.balance)
    
    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount

felix = User()
jess = User()
elijah = User()

felix.make_deposit(100)
felix.make_deposit(100)
felix.make_deposit(100)
felix.make_withdrawal(50)
felix.display_user_balance()

jess.make_deposit(300)
jess.make_deposit(100)
jess.make_withdrawal(50)
jess.make_withdrawal(50)
jess.display_user_balance()

elijah.make_deposit(200)
elijah.make_withdrawal(50)
elijah.make_withdrawal(50)
elijah.make_withdrawal(50)
elijah.display_user_balance()

felix.transfer_money(10000,elijah)
elijah.display_user_balance()
felix.display_user_balance()


