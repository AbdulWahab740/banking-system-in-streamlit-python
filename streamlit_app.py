import csv
import time
import random
from datetime import datetime
import streamlit as st
import requests
alpha_van_key = st.secrets["YOUR_ALPHA_VANTAGE_KEY"]

st.set_page_config(page_title="Abdul Wahab Banking System")
st.title("Hawkians Banking System💸🏦")
st.write("(Made by Abdul wahab)😎")
class Client:
    def __init__(self,Username, password, email):
        self.Username = Username
        self.password = password
        self.email = email
class Login:
    def __init__(self,Username,password): 
        self.Username= Username
        self.password = password

class Deposit:
    def __init__(self,acc_num, amount,):
        self.acc_num = acc_num
        self.amount = amount

class BankingSystem:
    def __init__(self,) :
        self.file_name_attr = None
        self.balance = 0

    def file_name(self, file_name):
        self.file_name_attr = file_name
        return self

    def is_username_exists(self, Username):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0] == Username:

                    return True
        return False           

    def is_password_exist(self, password):
        with open(self.file_name_attr,'r') as file:
            read = csv.reader(file)
            for row in read:
                if row and len(row) > 1 and row[1]== password:
                    return True
        return False

    def is_email_exists(self, email):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 2 and row[2] == email:
                    return True
        return False

    def write_to_csv(self, client):
        with open(self.file_name_attr, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([client.Username, client.password, client.email])
            print("Data has been written to the file.")

    def signin(self,Username, password, email):  
        client = Client(Username, password, email)
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
            st.write("Account has found. Successfully Logged in")

    def login(self,Username,password):
        client = Login(Username,password)
        self.write_to_logincsv(client)

    def read_from_csv(self):
        with open(self.file_name_attr, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # print(row)
                pass


def get_current_balance():
    return st.session_state.deposit_amount

def funds_deposit():
    deposit_input = st.text_input("Enter the deposit amount: ", key='deposit_input')
    if st.button("Deposit Amount") and is_valid_number(deposit_input):
        deposit_amount = float(deposit_input)
        st.write(f"You have deposited the amount of Rs:{deposit_amount}")
        st.session_state.deposit_amount = deposit_amount

def funds_withdrawal():
    withdrawal_input = st.text_input("Enter the amount you want to withdraw: ", key='withdrawal_input')
    if st.button("Withdraw Amount") and is_valid_number(withdrawal_input):
        withdrawal_amount = float(withdrawal_input)
        current_balance = get_current_balance()
        if withdrawal_amount <= current_balance:
            remaining_balance = current_balance - withdrawal_amount
            st.write(f"Your Balance Rs:{current_balance}")
            st.write(f"You have Withdrawn the amount of Rs:{withdrawal_amount}")
            st.write(f"Remaining balance: Rs:{remaining_balance}")
            st.session_state.deposit_amount = remaining_balance
        else:
            st.write("Insufficient funds for withdrawal.")
    # elif not is_valid_number(withdrawal_input):
    #     st.write("Enter a valid numeric input")

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def bill_payment():
    bill_opt = st.selectbox("Select the Bill you want to pay",['Select one','Electricity Bill','SUI Gas','WASA'])
    try: 
        if(bill_opt == "Electricity Bill" or bill_opt == "SUI Gas" or bill_opt == "WASA" ):
            bill_input = st.text_input("Enter the Amount of your Bill here: ",placeholder="Enter Here",key="bill_input")
            if st.button("Pay the Bill")and is_valid_number(bill_input):
                bill_amount = float(bill_input)
                current_balance = get_current_balance()
                if bill_amount <= current_balance:
                    remaining_balance = current_balance - bill_amount
                    st.write(f"Your Balance Rs: {current_balance}")
                    st.write(f"Bill Paid Rs: {bill_amount}")
                    st.write(f"Remaining Balance Rs: {remaining_balance}")
                    st.session_state.deposit_amount = remaining_balance
                else: 
                    st.write("Insufficient Amount of Money to pay bill!")
    except ValueError:
        st.write("Enter a Valid Input")

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={base_currency}&to_currency={target_currency}&apikey={api_key}'
    try:
        response = requests.get(url)
        data = response.json()

        if 'Realtime Currency Exchange Rate' in data:
            exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            return exchange_rate
        else:
            print('Unable to fetch exchange rate.')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None


def currency_exchange():
    currency_opt = st.selectbox("Select the Currency you want to convert",['Select one','US Dollar','EURO','UK Pound'])
    if currency_opt == "US Dollar":
        api_key = alpha_van_key
        base_currency = 'USD'
        target_currency = 'PKR'
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

        
        dollar_input = st.text_input("Enter the Amount of Money you want to Convert: ",placeholder="Enter Here",key="dollar_input")
        if st.button("Convert")and is_valid_number(dollar_input):
                if exchange_rate is not None:
                    st.write(f'The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}')    
                dollar_amount = float(dollar_input)
                current_balance = get_current_balance()
                if dollar_amount <= current_balance:
                    in_dollar = dollar_amount/exchange_rate
                    remaining_balance = current_balance - dollar_amount
                    st.write(f"Your Balance is Rs: {current_balance}")
                    st.write(f"Amount you want to convert Rs: {dollar_amount}")
                    st.write(f"Amount in Dollars $: {in_dollar}")
                    st.write(f"Your Remaining Balance in rupee is Rs: {remaining_balance}")
                    st.session_state.deposit_amount = remaining_balance
                else:
                    st.write("Insufficient Amount to Convert in dollar")


    elif currency_opt == "EURO":
        eu_input = st.text_input("Enter the Amount of Money you want to Convert: ",placeholder="Enter Here",key="eu_input")
        api_key = alpha_van_key
        base_currency = 'EUR'
        target_currency = 'PKR'
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        
        if st.button("Convert")and is_valid_number(eu_input):
                if exchange_rate is not None:
                    st.write(f'The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}')
                eu_amount = float(eu_input)
                current_balance = get_current_balance()
                if eu_amount <= current_balance:
                    in_eu = eu_amount/exchange_rate
                    remaining_balance = current_balance - eu_amount
                    st.write(f"Your Balance is Rs: {current_balance}")
                    st.write(f"Amount you want to convert Rs: {eu_amount}")
                    st.write(f"Amount in EURO €: {in_eu}")
                    st.write(f"Your Remaining Balance in rupee is Rs: {remaining_balance}")
                    st.session_state.deposit_amount = remaining_balance
                else:
                    st.write("Insufficient Amount to Convert in EURO")
    elif currency_opt == "UK Pound":
        pound_input = st.text_input("Enter the Amount of Money you want to Convert: ",placeholder="Enter Here",key="pound_input")
        api_key = alpha_van_key
        base_currency = 'EUR'
        target_currency = 'PKR'
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        if st.button("Convert")and is_valid_number(pound_input):
                if exchange_rate is not None:
                    st.write(f'The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}')
                pound_amount = float(pound_input)
                current_balance = get_current_balance()
                if pound_amount <= current_balance:
                    in_pound = pound_amount/exchange_rate
                    remaining_balance = current_balance - pound_amount
                    st.write(f"Your Balance is Rs: {current_balance}")
                    st.write(f"Amount you want to convert Rs: {pound_amount}")
                    st.write(f"Amount in pound ₤: {in_pound}")
                    st.write(f"Your Remaining Balance in rupee is Rs: {remaining_balance}")
                    st.session_state.deposit_amount = remaining_balance
                else:
                    st.write("Insufficient Amount to Convert in Pound")
if __name__ == "__main__":
    bank = BankingSystem()
    Signin = BankingSystem()
    login = BankingSystem()
    Signin.file_name('signin_data.csv')
    login.file_name("login_data.csv")
    with st.sidebar:
        st.write("Have an Account in Hawkian Banking?")
        options_st = st.selectbox("Select the following: ", ['Select one','SignUp', 'Login'],)
        if options_st == 'SignUp':
            csv_handler = Signin
            while True:
                username_key = 'username_2'
                Username = st.text_input("Enter Your Username: ", key=username_key)
                password_key = 'password_2'
                password = st.text_input("Enter Your Password: ", key=password_key,placeholder="********")
                try:
                    count = 0
                    for i in password:
                        count+=1
                    
                    if(count<8):
                        st.write("Input the minimum of 8 word password")
                    if csv_handler.is_password_exist(password):
                        st.write("Password already exists")
                except ValueError:
                    pass

                email = st.text_input("Enter Your e-mail: ",placeholder='*****@gmail.com')
                try:
                    if "@gmail.com" not in email:
                        st.write("Enter the correct email address")
                except ValueError:
                    pass
                break
            if st.button("Submit"):
                st.write("We are generating your Account.... ")
                time.sleep(2)
                acc_num = int(''.join(map(str, [random.randint(1, 10) for _ in range(10)])))
                st.write("Your Account Number is: ", acc_num)
                csv_handler.signin(Username, password, email)
                csv_handler.read_from_csv()
        elif options_st == 'Login':
            csv_handler = Signin
            login_handler = login.file_name('login_data.csv')
            time.sleep(1)
            while True:
                username_key = 'username_1'
                Username = st.text_input("Enter Your Username: ", key=username_key)
                if csv_handler.is_username_exists(Username):
                    st.write("This username exist!")
                password_key = 'password_1'
                password = st.text_input("Enter Password Here: ", key=password_key)
                if st.button("Login"):
                    login_handler.login(Username, password)
                    login_handler.read_from_csv()
                break

    if 'deposit_amount' not in st.session_state:
        st.session_state.deposit_amount = 0

    select = st.selectbox("Select the functionality to access:", ["Select One","1.Funds Deposit", "2.Funds Withdrawal", "3.Bill Payments", "4.Bank Balance", "5.Foreign Currency Exchange"])

    if select == "1.Funds Deposit":
        funds_deposit()
    elif select == "2.Funds Withdrawal":
        funds_withdrawal()
    elif select == "3.Bill Payments":
        bill_payment()
    elif select == "4.Bank Balance":
        balance = get_current_balance()
        st.write(f"Your Current Balance is Rs: {balance}")
    elif select == "5.Foreign Currency Exchange":
        currency_exchange()