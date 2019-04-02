class User:		# declare a class and give it name User
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rage=0.02, balance=0)

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        if self.account_balance >= 0:
            print(f"User: {self.name}, Balance: ${round(self.account_balance,2)}")
            return self
        else: 
            print(f"User: {self.name}, Balance: -${round(self.account_balance*-1,2)}")
            return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} has successfully transferred ${amount} to {other_user.name}")
        return self

    class BankAccount:
        def __init__(self,int_rate,balance):
            self.int_rate = 0.006
            self.balance = 0

        def deposit(self,amount):
            self.balance += amount
            return self

        def withdraw(self,amount):
            if self.balance - amount > 0:
                self.balance -= amount
            else:
                print("Insufficient funds: Charging a $5 fee.")
                self.balance -= 5
            return self

        def display_account_info(self):
            if self.balance >= 0:
                print(f"Balance: ${round(self.balance,2)}")
            else:
                print(f"Balance: -${round(self.balance*-1,2)}")
            return self

        def yield_interest(self):
            if self.balance >= 0:
                self.balance *= (1+self.int_rate)
            return self


#nina = User("Nina Gervaise Tompkin","nina.tompkin@gmail.com")
#guido = User("Guido Von Trapperson","italian_stallion@gmail.com")
#dimitar = User("Dimitar Mi Ho","dimho@gmail.com")

    ninaAccount = BankAccount("0.006","5000")
    guidoAccount = BankAccount("0.05","1000")

    ninaAccount.deposit(400).deposit(12.99).deposit(35.23).withdraw(300).yield_interest().display_account_info()
    guidoAccount.deposit(200).deposit(300).withdraw(100).withdraw(40.23).withdraw(19.99).withdraw(99.99).yield_interest().display_account_info()


#nina.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(300).display_user_balance()

#dimitar.make_deposit(42.32).make_deposit(59.99).make_withdrawl(24.99).make_withdrawl(6.60).display_user_balance()

#guido.make_deposit(1024.41).make_withdrawl(543.20).make_withdrawl(42.31).make_withdrawl(245.99).display_user_balance()

#nina.transfer_money(guido,200).display_user_balance()
#guido.display_user_balance()