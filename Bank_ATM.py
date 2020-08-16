''' A program to simulate ATM function to display customer account details ,
withdraw Money and Deposit Money'''


# bnk Account class to handle all type of transaction and for creation of bank accounts
class BankAccount():

    global account_details
    account_details = {}

    def __init__(self,CustomerId, Name, Amount,Account_Type):
        self._CustomerId = CustomerId
        self._Name = Name
        self._TotalAmount = Amount
        self._Account_Type = Account_Type
        self.Add_Account(int(self._CustomerId),self._Name,float(self._TotalAmount),self._Account_Type)

    def Account_details (cust_id):

        print("Existing details of your account is as follows : ")
        print(f"customer Id : {cust_id}")
        print(f"Available Balance : {account_details[cust_id][1]}")
        print(f"Account Type : {account_details[cust_id][2]}")

    def deposit(cust_id,deposit_Amount):
        account_details[cust_id][1] = account_details[cust_id][1] + deposit_Amount

    def withdrawl(cust_id,withdrawl_Amount):
        account_details[cust_id][1] = account_details[cust_id][1] - withdrawl_Amount

    def Check_balance(cust_id):
        print(f"Current Available Balance : {account_details[cust_id][1]}")

    def Add_Account(self, Cust_id, Name, Amount, Account_type):

        account_details[Cust_id] = [Name,Amount,Account_type]

    def Customer_Id_Validation(cust_id):

        if (cust_id in account_details.keys()):
            return True
        else:
            return False

def initialize():

    BankAccount(1, 'Shaily', 10000, 'Savings')
    BankAccount(2, 'Shyam', 10000, 'Current')
    BankAccount(3, 'Shubhi', 10000, 'Business')

def main() :

    initialize()
    Cust_id = int(input('Enter Your customer ID : '))

    if ( BankAccount.Customer_Id_Validation(Cust_id) == True ) :

        print(f"Welcome {account_details[Cust_id][0]} ")
        continue_transaction ='Y'

        while ( continue_transaction.upper() == 'Y'):

            while True:
                print ("Enter 1 for Deposit into account")
                print ("Enter 2 for with-drawl from account")
                print ("Enter 3 for check Account Balance")
                input_type = input("Waiting for Input: ")
                if input_type in ('1','2','3') :

                    if (input_type == '1'):
                        deposit_Amount = float(input("How much Amount you want to deposit : "))
                        BankAccount.deposit(Cust_id,deposit_Amount)
                        BankAccount.Check_balance(Cust_id)
                    if (input_type == '2'):
                        while True:
                            withdrawl_Amount = float(input("How much Amount you want to withdraw : "))
                            if(account_details[Cust_id][1] < withdrawl_Amount):
                                print(" You cannot withdraw amount higher than your Available Balance")
                                BankAccount.Check_balance(Cust_id)
                                print("Please re-enter withdraw amount !! ")
                                continue
                            else:
                                BankAccount.withdrawl(Cust_id, withdrawl_Amount)
                                BankAccount.Check_balance(Cust_id)
                                break

                    if (input_type == '3'):
                        BankAccount.Account_details(Cust_id)
                    break
                else:
                    print("Invalid Input !! Please re-enter")
                    continue
            continue_transaction = input("Wanted to Continue with Next Transaction ( Y/N ) : ")
        else:
            print("Thank You")
    else:

        print("Sorry ! invalid customer ID entered")

main()