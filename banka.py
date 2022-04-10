from time import sleep
from os import system

class Customer:
    def __init__(self, name:str, surname:str, idno:str, password:str):
        self.__name = name
        self.__surname = surname
        self.__idno = idno
        self.__password = password
        self.__balance = 0

    def getName(self):
        return self.__name

    def getSurname(self):
        return  self.__surname

    def getIdno(self):
        return  self.__idno

    def getPassword(self):
        return  self.__password

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount:float):
        self.__balance = amount

class Bank:
    def __init__(self,name:str):
        self.__name = name
        self.__customers = list()

    def customerLogin(self,idno:str,password:str):
        for i in self.__customers:
            if i.getIdno() == idno and i.getPassword() == password:
                return i
        return False

    def customerExists(self,idno:str):
        for i in self.__customers:
            if i.getIdno() == idno:
                return i
        return False

    def transferMoney(self, sender:Customer, reciever:Customer, amount:float):
        if sender in self.__customers and reciever in self.__customers:
            if sender.getBalance() >= amount:
                sender.setBalance(sender.getBalance() - amount)
                reciever.setBalance(reciever.getBalance() + amount)
            else:
                print("Balance not enaugh!")
        else:
            print("Customer not found!")

    def becomeCustomer(self,name:str, surname:str, idno:str, password:str):
        self.__customers.append(Customer(name,surname,idno,password))

    def withdraw(self, customer:Customer, amount:int):
        if amount % 10 == 0:
            if customer.getBalance() > amount:
                print("Do not forget to take your money!")
                customer.setBalance(customer.getBalance() - amount)
            else:
                print("Balance not enaugh!")
        else:
            print("Please enter amount 10 and 10x")

    def deposit(self,customer:Customer,amount:int):
        if amount % 5 != 0:
            print("Please add money 5 and 5X do not use changes!")
        else:
            customer.setBalance(customer.getBalance() + amount)

    def balanceInfo(self,customer:Customer):
        print("""
        Name : \t {}
        Surname : \t {}
        Id : \t {}
        Balance : {}
        """.format(customer.getName(),customer.getSurname(),customer.getIdno(),customer.getBalance()))



def main():
    bank = Bank("Isbank")
    while True:
        system("cls")
        print("""
        [1] Be a Customer
        [2] Login
        [3] Exit
        """)

        choice = input("Enter your choice :")

        if choice == "3":
            quit()
        elif choice == "1":
            name = input("Name :")
            surname = input("Surname :")
            idno = input("Id :")
            password = input("Password :")
            bank.becomeCustomer(name,surname,idno,password)
            input("Press enter to return to the Main menu")
        elif choice == "2":
            idno = input("ID : ")
            password = input("password :")
            if bank.customerLogin(idno,password):
                customer = bank.customerLogin(idno,password)
                while True:
                    system("cls")
                    print("""
    [1] Show Balance        [2] Deposit
    
    [3] WithDraw Money      [4] Transfer
                [Q] Exit                
                    """)
                    choice2 = input("Enter your Choice :")
                    if choice2 == "1":
                        bank.balanceInfo(customer)
                        input("Press enter to return to the Main menu")
                    elif choice2 == "2":
                        amount = int(input("Enter the money amount 5x"))
                        bank.deposit(customer, amount)
                        input("Press enter to return to the Main menu")
                    elif choice2 == "3":
                        amount = int(input("Enter the money amount 10x"))
                        bank.withdraw(customer,amount)
                        input("Press enter to return to the Main menu")
                    elif choice2 == "4":
                        id = input("Enter the Reciever ID")
                        amount = float(input("Enter the amount to transfer"))
                        if bank.customerExists(id):
                            reciever = bank.customerExists(id)
                            bank.transferMoney(customer,reciever,amount)
                        else:
                            print("Customer ID not Exists")
                        input("Press enter to return to the Main menu")
                    elif choice2 == "Q" or choice2 == "q":
                        print("Switching to main menu")
                        sleep(2)
                        break
                    else:
                        print("Invalid Choice")
        else:
            print("Wrong login Id password or customer not Exist!")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()