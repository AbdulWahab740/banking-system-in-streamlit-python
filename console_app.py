import csv
import time
import random
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Abdul Wahab Banking System")
st.title("Hawkians Banking System")
st.write("(Made by Abdul wahab)")
class Client:
    def __init__(self, f_name, l_name, cnic, phNo, Username, password, email,acc_num):
        self.f_name = f_name
        self.l_name = l_name
        self.cnic = cnic
        self.phNo = phNo
        self.Username = Username
        self.password = password
        self.email = email
        self.acc_num = acc_num


class Login:
    def __init__(self,Username,password): 
        self.Username= Username
        self.password = password

class Credit:
    def __init__(self,acc_no):
        self.acc_no = acc_no

class Deposit:
    def __init__(self,acc_num, amount, datetime, transaction_Id):
        self.acc_num = acc_num
        self.amount = amount
        self.datetime = datetime
        self.transaction_Id = transaction_Id

class Withdraw:
    def __init__(self,withdrawal,datetime,transaction_Id) :
        self.withdrawal = withdrawal
        self.datetime =datetime
        self.transaction_Id = transaction_Id
class BankingSystem:
    def __init__(self,) :
        self.file_name_attr = None
        self.balance = 0

    def file_name(self, file_name):
        self.file_name_attr = file_name
        return self
    def withdrawal(self, acc_num, amount, datetime, transaction_Id):
                    if self.is_acc_num_exist(acc_num):
                        acc_row = self.get_account_row(acc_num)
                        if acc_row:
                            acc_balance = int(acc_row[8])  # Assuming amount is at index 8
                            if acc_balance >= amount:
                                new_balance = acc_balance - amount
                                acc_row[8] = str(new_balance)  # Update the balance
                                self.update_account_row(acc_row)
                                wd = Withdraw(amount, datetime, transaction_Id)
                                self.withdrawal_file(wd)
                            else:
                                print("Insufficient funds")
                        else:
                            print("Account not found")
                    else:
                        print("Account not found")
                      
    def get_account_row(self, acc_num):
                  with open(self.file_name_attr, 'r') as file:
                        read = csv.reader(file)
                        for row in read:
                            if row and len(row) > 7 and row[7]== acc_num:
                                return row
    def update_account_row(self, updated_row):
                    rows = []
                    with open(self.file_name_attr, 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if row and len(row) > 7 and row[7] == updated_row[7]:  # Assuming account number is at index 7
                                rows.append(updated_row)
                            else:
                                rows.append(row)
                    with open(self.file_name_attr, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)

    # def withdrawal_file(self, withdraw):
    #     with open(self.file_name_attr, 'a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([withdraw.amount, withdraw.datetime, withdraw.transaction_Id])

    def deposit(self,acc_num,amount,datetime,transaction_Id,):

        dep = Deposit(acc_num,amount,datetime,transaction_Id,)
        self.update_signin_file(dep)
        # self.write_to_deposit_Account_csv(dep)

    def update_signin_file(self, deposit):
        with open(self.file_name_attr, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([deposit.acc_num, deposit.amount, deposit.datetime, deposit.transaction_Id])

    def is_username_exists(self, Username):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 4 and row[4] == Username:

                    return True
        return False           

    def is_password_exist(self, password):
        with open(self.file_name_attr,'r') as file:
            read = csv.reader(file)
            for row in read:
                if row and len(row) > 5 and row[5]== password:
                    return True
        return False

    def is_phno_exists(self, phNo):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 3 and row[3] == phNo:
                    return True
        return False
    def is_email_exists(self, email):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 6 and row[6] == email:
                    return True
        return False
    def is_cnic_exist(self, cnic):
        with open(self.file_name_attr,'r') as file:
            read = csv.reader(file)
            for row in read:
                if row and len(row) > 2 and row[2]== cnic:
                    return True
        return False
    def is_acc_num_exist(self, acc_num):
        with open(self.file_name_attr,'r') as file:
            read = csv.reader(file)
            for row in read:
                if row and len(row) > 7 and row[7]== acc_num:

                    return acc_num
        return False

    def write_to_csv(self, client):
        with open(self.file_name_attr, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([client.f_name, client.l_name, client.cnic, client.phNo, client.Username, client.password, client.email,client.acc_num])
            print("Data has been written to the file.")

    def signin(self, f_name, l_name, cnic, phNo, Username, password, email,acc_num):  
        client = Client(f_name, l_name, cnic, phNo, Username, password, email,acc_num)
        self.write_to_csv(client)
    def acc_num_ver(self):
        with open(self.file_name_attr,'r') as file:
                read = csv.reader(file)
                for row in read:
                    if row and len(row) > 7 and row[7]== acc_num:
                        print(acc_num)
    def write_to_logincsv(self, client):
        with open(self.file_name_attr, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([client.Username, client.password])
            print("Data has been written to the file.")

    def login(self,Username,password):
        client = Login(Username,password)
        self.write_to_logincsv(client)

    def read_from_csv(self):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # print(row)
                pass

    def account_type(self):

        while True:
            option = input("Which Account Type you want to Create\n1.Credit Account\n2.Debit Account\n3.Savings Account\n Enter the Number of your desired Account here: ")
            if option == '1':
                time.sleep(1)
                print("Your Credit Account has been created")
                break
            elif option == '2':
                time.sleep(1)
                print("Your Debit Account has been created")
                self.credit_account()
                break
            elif option == '3':
                time.sleep(1)
                print("Your Savings Account has been created")
                break
            else:
                time.sleep(1)
                print("!!Enter The Correct the Number!!")
                time.sleep(1)
                continue

    def credit_account(self,acc_no):        
        acc_Num = Credit(acc_no)
        self.write_to_Credit_Account_csv(acc_Num)

    def write_to_Credit_Account_csv(self, client):
        with open(self.file_name_attr, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([client.acc_no])


    def debit_account(self):
        pass
    def saving_account(self):
        pass

if __name__ == "__main__":

    print("<------Welcome To the Hawkians Banking LTD.------->")
    time.sleep(2)
    print("\n\n Did you Have an Account in the Bank?\n")
    time.sleep(1)
    print("Write 1 for signup\nWrite 2 for login")
    bank = BankingSystem()
    Signin = BankingSystem()
    login = BankingSystem()
    deposit = BankingSystem()
    withdraw= BankingSystem()

    Signin.file_name('signin_data.csv')
    login.file_name("login_data.csv")
    deposit.file_name("deposit_amount.csv")
    withdraw.file_name("Withdraw.csv")
    # credit.file_name("Account_Number.csv")
    

    acc_exist = int(input("Write here: "))
    if acc_exist == 1:
        csv_handler = Signin
        f_name = input("Enter your first Name: ")
        l_name = input("Enter your last Name: ")

        while True:

                    Username = input("Enter Your Username: ")

                    if csv_handler.is_username_exists(Username):
                        print("User name already exist! Please Choose another username")
                        continue
                    password = input("Enter Your Password: ")
                    if csv_handler.is_password_exist(password):
                        print("Password already exist")
                        continue

                    cnic = (input("Enter Your CNIC Number: "))
                    if csv_handler.is_cnic_exist(cnic):
                        print("This CNIC already exist! Please Choose another CNIC")
                        continue
                    phNo = input("Enter Your Phone Number: ")
                    if csv_handler.is_phno_exists(phNo):
                        print("This Phone Number already exist! Please Choose another Phone Number")
                        continue
                    email = input("Enter Your e-mail: ")
                    if csv_handler.is_email_exists(email):
                        print("This e-mail already exist! Please Choose another e-mail")
                        continue        
                    break
        time.sleep(1)
        bank.account_type()
        acc_num = int(''.join(map(str, [random.randint(1, 10) for _ in range(10)])))
        print("Your Account Number is: ", acc_num)

        csv_handler.signin(f_name, l_name, cnic, phNo, Username, password, email,acc_num)
        csv_handler.read_from_csv()

    elif acc_exist == 2:
        time.sleep(1)
        csv_handler = Signin
        login_handler = login.file_name('login_data.csv')
        print("Let's Logged in")
        time.sleep(1)
        while True:  
            Username = input("Enter Your Username: ")
            if csv_handler.is_username_exists(Username):
                print("This username exist!")
            else:
                print("Wrong Username")
                continue

            password = input ("Enter Password Here: ")
            if csv_handler.is_password_exist(password):
                print("Correct Password")              
            else:
                print("Wrong Password")
                continue

            login_handler.login(Username,password)
            login_handler.read_from_csv()
            break
    time.sleep(2)

    while True:
        time.sleep(2)
        print("\n\nWhat Functionality you want to use\n1.Funds Deposit\n2.Funds Withdrawal\n3.Bill Payments\n4.Bank Balance\n5.Foreign Currency Exchange")
        # print("5.Cards Management\n6.Shares and Stocks\n\n8.Alerts and Notifications\n9.Loans Management\n10.Transection Limits11.Transection History\n12.Users Feedback\n13.Customer Care and Services")
        select = int(input("\nEnter The Number Of Functionality here: "))

                ## <------ Deposit ------->

        if select == 1:
            deposit_csv = deposit
            while True:
                try:
                    deposit_amount = float(input("Enter the deposit amount: "))
                    break  # Break the loop if the input is a valid float
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            choice = (input("\n\nDo you want to re-use the system?(y/N): "))
            if (choice.lower()=='y'):
                continue
            else:
                break

        ## <------ Withdrawal ------->
       
        elif select ==  2:
            while True:
                try:
                    withdrawal_amount = float(input("Enter the withdrawal amount: "))
                    break  # Break the loop if the input is a valid float
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"Bank Balance: {deposit_amount}")
            print(f"Withdrawal amount: {withdrawal_amount}")
            remaining_balance = deposit_amount - withdrawal_amount
            print(f"Remaining balance: {remaining_balance}")
            deposit_amount = remaining_balance
            choice = (input("\n\nDo you want to re-use the system?(y/N): "))
            if (choice.lower()=='y'):
                continue
            else:
                break
                
        ## <------ Bill Payment ------->
            
        elif(select==3):
            while True:
                try:
                    payment = input("Which bill payment you want to do?\n1. Electricity Bills\n2. WASA Bills\n3. SUI Gas Bills\nWrite here: ")
                    if (payment == '1' or payment == '2' or payment == '3'):
                        bill_pay = int(input("Enter the amount of your bill: "))
                        if(bill_pay>deposit_amount):
                            print("Don't Have Enough Money💰")
                        else:
                            deposit_amount = deposit_amount-bill_pay
                            print(f"Your Bill of {bill_pay} has been paid!")
                            print(f"Current Balance {deposit_amount}")
                        break
                    else:
                        print("Enter the Valid Input!!!!")
                except ValueError:
                    print("Enter the Valid Amount")
            choice = (input("\n\nDo you want to re-use the system?(y/N): "))
            if (choice.lower()=='y'):
                continue
            else:
                break

                ## <------ Bank Balance ------->
            
        elif(select==4):
            print("You Want to Know your Bank Balance")
            time.sleep(0.5)
            print(f"\nYour Bank Balance is : {deposit_amount}")
 
               ## <------ Currency Exchange ------->
        elif(select==5):
            while True:
                try:
                    C1 = int(input("Enter the amount of money you want to convert(in rupee): "))
                    to_which = input("Enter the currency to which you want to convert\n1. US Dollar\n2. Euro\n3. Pound\nEnter the number here: ")
                    if(to_which == '1'):                        
                        usd = C1/278
                        print(f"Your Currency has been converted to US Dollar\nThe Amount is {usd}")
                    elif(to_which == '2'):                        
                        eu = C1/300
                        print(f"Your Currency has been converted to Euro \nThe Amount is {eu}")
                    elif(to_which == '3'):
                        po = C1/351
                        print(f"Your Currency has been converted to UK Pound\nThe Amount is {po}")
                except ValueError:
                    print("Enter the Valid Input~!!!!!!!!!!!")

