
# Encapsulation
# ~~~~~~~~~~~~~
# Wrapping data and functions into a single unit (object)

# create account class with 2 attributes - balance and account no.
# create methods for debit,credit and printing the balance

class Account:
    def __init__(self,acc,bal = 0):
        self.account_no = acc # this is bydefault public
        self.__balance = bal  # making balance private just by adding two underscore "__" before attribute name

    def debit(self,amount):
        if(amount > self.__balance or amount < 0):
            print("Enter Correct debit amount .")
            return
        self.__balance -= amount
        print("Rs", amount, "is debited.")
        self.__checkBalance()

    def credit(self, amount):
        if(amount < 0):
            print("Enter Correct credit Amount.")
            return 
        self.__balance += amount
        print("Rs", amount,"is credited.")
        self.__checkBalance()

    def __checkBalance(self):                   #private function
        print("Current balance:",self.__balance)

acc1 = Account("123456789",10000)
acc1.credit(500)
acc1.debit(50)
acc1.credit(-500)
acc1.debit(1000000)
acc1.debit(-500)
print(acc1.account_no)


del acc1 #deleting acc1