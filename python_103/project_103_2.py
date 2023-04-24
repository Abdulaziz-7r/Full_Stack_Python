import datetime as dt
class Bank():
    def __init__(self,name):
        self.name = name

    def get_bank_name(self):
        print(self.name)
    
    def set_bank_name(self,name):
        self.name = name
        print(f'new bank name is {name}')

class User(Bank):
    def __init__(self,f_name,l_name,phone_num,bank_name):
        super().__init__(bank_name)
        self.f_name = f_name
        self.l_name = l_name
        self.phone_num = phone_num
    
    def get_f_name(self):
        return self.f_name

    def get_l_name(self):
        return self.l_name

    def get_phone_num(self):
        return self.phone_num
    
    def set_f_name(self,f_name):
        self.f_name = f_name
        print(f'first name changed to {f_name}')

    def set_l_name(self,l_name):
        self.l_name = l_name
        print(f'last name changed to {l_name}')

    def set_phone_num(self, phone_num):
        self.phone_num = phone_num
        print(f'phone number changed to {phone_num}')

class Account(User):
    account_num = 0
    balance = 0
    login = False
    def __init__(self, password, f_name, l_name, phone_num, bank_name):
        super().__init__(f_name,l_name,phone_num,bank_name)
        self.account_num += 1
        self.password = password
    
    def set_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def check_password(self,password):
        if self.password == password:
            self.login = True
        else:
            print('Password in not correct')
        return self.login

    def deposit(self,amount):
        if not self.login:
            print('Please enter your password first')
            return
        self.balance +=amount
        date = dt.datetime.now()
        print(f'{amount} deposited successfully to your bank account in {date.strftime("%A, %d %B %Y")}, at {date.strftime("%I:%M%p")}')

    def withdraw(self, amount):
        if not self.login:
            print('Please enter your password first')
            return
        if self.balance < amount:
            print(f'sorry you can not withdraw this amount your account balance is {self.balance}')
        else:
             date = dt.datetime.now()
             self.balance -= amount
             print(f'{amount} withdrawn successfully from your bank account in {date.strftime("%A, %d %B %Y")}, at {date.strftime("%I:%M%p")}')
    
    def check_balance(self):
        if not self.login:
            print('Please enter your password first')
            return
        print(f'your current balance is {self.balance}')


############################## 
def main():
    account1 = Account( password = 1900, f_name= 'Abdulaziz', l_name='Alharthi', phone_num='12345', bank_name= "Alinma")
    password = int(input('Enter your password: '))
    while (True):
        if not account1.check_password(password):
            password = int(input('Enter your password: '))
            continue
        amount = 0
        selection = input("Please Select Transaction \n 1- Withdrawal \n 2- Deposit \n 3- Balance Enquiry \n 4- Exit \n")
        match selection:
            case '1':
                amount = int(input('Please enter withdraw amount: '))
                account1.withdraw(amount)
            case '2':
                amount = int(input('Please enter deposit  amount: '))
                account1.deposit(amount)
            case '3':
                account1.check_balance()
            case '4':
                break


if __name__ == '__main__':
    main()
    