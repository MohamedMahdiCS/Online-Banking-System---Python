#MOHAMED MAHMOUD SAID
#TP066611


def login():
    print("Welcome to APU Online Banking System")
    User = input("Please enter 'a' for Admin or 'c' for Customer:")
    while User !='a' and User !='c':
        print("You have entered an invalid access code.")
        login()
        break
    else:
        if User == 'a':
            admin()
        elif User == 'c':
            Customerlogin()

def admin():
    print("\nDear admin, please enter your login credential.")
    userid = input("Please enter user login ID:")
    userpwd = input("Please enter your Password:")
    flg = "0"
    with open("adminDetails.txt", 'r') as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if userid == reclist[0] and userpwd == reclist[1]:
                flg = reclist
                break
        if flg == "0":
            print("Access Denied. Invalid admin login credential")
        else:
            print("\n Welcome APUAdmin!! Do you wish to continue?\nEnter '5' to continue, any other number to terminate: ")
            cont = input("")
            if cont != '5':
                print("Have a nice day")
                login()
            else:
                while True:
                    print("\n****WELCOME TO APU BANKING SERVICE SYSTEM****\n1.Customer onboarding\n2.View all Customer Details\n3.View Customer Transaction\n4.Create Admin Accounts\n5.Cstatementofaccountreport\n6.Logout the system\nPlease selecet which option you would like to perform (1/2/3/4/5/6): ")
                    action = input("")
                    if action == '1':
                        Customeronboarding()
                    elif action == '2':
                        View_Customer_Details()
                    elif action == '3':
                        View_Customer_Transaction()
                    elif action == '4':
                        Create_admin_Account()
                    elif action == '5':
                        Cstatementofaccountreport()
                    elif action == '6':
                        login()
                    else:
                        print("Invaild access code")
        return flg


def Customerlogin():
    print("\n Dear customer, please enter your login credential: ")
    Userid = input("ID: ")
    Userpw = input("Password: ")
    flg = "0"
    with open("custdetails.txt", 'r') as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if Userid == reclist[0] and Userpw == reclist[1]:
                flg = reclist
                break
        if flg == "0":
            print("Access Denied. Invalid LoginID or Password.")
            Customerlogin()
        else:
            print("\nWelcome! Do you wish to continue?\n Enter '5' to continue, any other number to Terminate: ")
            cont = input("")
            while cont != '5':
                print("Have a nice day")
                login()
            else:
                    while True:
                        print("\nWelcome! \n****MAIN MENU****\n\t1.Deposit\n\t2.Withdrawal\n\t3.reset_password\n\t4.Logout the system\nplease select the action you would like to perform (1/2/3/4): ")
                        action = input("")
                        if action == '1':
                            deposit()
                        elif action == '2':
                            Withdraw()
                        elif action == '3':
                            reset_password()
                        elif action == '4':
                            login()
                        else:
                            print("Invaild access code")
        return flg



def Customeronboarding():
  newcust = []
  print("Create new customer account")
  custID = input("Customer ID: ")
  custName = str(input("Customer Name: "))
  custPassword = input("Password: ")
  accBal = input("Available Balance: ")
  gender = input("Gender(M/F): ")
  custDOB = input("Date of birth(DDMMYYYY): ")
  accType = input("Account Type(s/c): ")
  accEmail = input("Email address: ")
  a = print("LoginID\t:", custID, "\nPassword\t:", custPassword, "\nGender(M/F)\t:", gender, "\nDate of Birth\t\t:",custDOB, "\nAvailable Balance\t\t:", float(accBal), "\nAccount name\t\t:", custName,"\nAccount type (s/c)\t\t:", accType, "\nEmail Address\t\t:", accEmail)
  print("\nAccount has been created successfully")
  with open("custdetails.txt", "a") as fh:
    rec = custID + ":" + custPassword + ":" + custName + ":" + accType + ":" + custDOB + ":" + gender + ":" + accEmail + ":" + accBal + "\n"
    newcust.append(rec)
    fh.write(str(newcust))
    fh.close()
    print("Do you want to perform other action(2/3/4/5/6)?")
    otheraction = input("")
    if otheraction == '2':
        View_Customer_Details()
    elif otheraction == '3':
        View_Customer_Transaction()
    elif otheraction == '4':
        Create_admin_Account()
    elif otheraction == '5':
        Cstatementofaccountreport()
    elif otheraction == '6':
        login()
    else:
        print("Invalid action.")
        admin()



def View_Customer_Details():
    print("***View Customer Profile***\n")
    with open("custdetails.txt", "r") as fh:
        print("=" * 135)
        print("User ID".ljust(13)+"|"+"User Password".ljust(15)+"|"+"User Name".ljust(15)+"|"+"Account Type".ljust(15)+"|"+"Date of birth(DDMMYYYY)".ljust(15)+"|" +"Gender(M/F)".ljust(15)+"|"+"Email address".ljust(15)+"|"+"Account Balance")
        print("=" * 135)
        for rec in fh:
            reclist = rec.strip("\n").split(":")
            print(reclist[0].ljust(13)+"|"+reclist[1].ljust(15)+"|"+reclist[2].ljust(15)+"|"+reclist[3].ljust(15)+"|"+reclist[4].ljust(25)+"|"+ reclist[5].ljust(15)+"|"+reclist[6].ljust(15)+"|"+reclist[7],"\n")
    print("Do you want to perform other action(1/3/4/5/6)?")
    otheraction = input("")
    if otheraction == '1':
        Customeronboarding()
    elif otheraction == '3':
        View_Customer_Transaction()
    elif otheraction == '4':
        Create_admin_Account()
    elif otheraction == '5':
        Cstatementofaccountreport()
    elif otheraction == '6':
        login()
    else:
        print("Invalid action.")
        admin()

def View_Customer_Transaction():
    print("***View Customer Transaction***\n")
    with open("transaction.txt", "r") as fh:
      print("=" * 100)
      print("User ID".ljust(15)+"|"+"Transaction Date".ljust(15)+"|"+"Transaction Type".ljust(15)+"|"+"Transaction Amount".ljust(15)+"|"+"Account Type".ljust(15)+"|"+"Account Balance")
      print("=" * 100)
      for rec in fh:
          reclist = rec.strip("\n").split(":")
          print(reclist[0].ljust(15)+"|"+reclist[1].ljust(15)+"|"+reclist[2].ljust(15)+"|"+reclist[3].ljust(15)+"|"+reclist[4].ljust(15)+"|"+reclist[5],"\n")
    print("Do you want to perform other action(1/2/4/5/6)?")
    otheraction = input("")
    if otheraction == '1':
        Customeronboarding()
    elif otheraction == '2':
        View_Customer_Details()
    elif otheraction == '4':
        Create_admin_Account()
    elif otheraction == '5':
        Cstatementofaccountreport()
    elif otheraction == '6':
        login()
    else:
        print("Invalid action.")
        admin()


def Create_admin_Account():
    newadmin = []
    print("***Welcome to the default super user account menu!***")
    print("You may create a new admin account!")
    print("Enter new admin details:")
    name = str(input("Admin Name: "))
    pwd = input("Password: ")
    gender = input("Gender(M/F): ")
    DOB = input("Date of birth(DDMMYYYY): ")
    accNo = input("Account Number: ")
    a = print("Admin Name\t:", name, "\nPassword\t:", pwd, "\nGender(M/F)\t:", gender, "\nDate of Birth\t\t:", DOB,"\nAccount Number\t\t:", accNo)
    print("\nAccount has been created successfully")
    with open("adminDetails.txt", "a") as fh:
        rec = name + ":" + pwd + ":" + gender + ":" + DOB + ":" + accNo + "\n"
        newadmin.append(rec)
        fh.write(str(newadmin))
        fh.close()
    print("Do you want to perform other action(1/2/3/5/6)?")
    otheraction = input("")
    if otheraction == '1':
        Customeronboarding()
    elif otheraction == '2':
        View_Customer_Details()
    elif otheraction == '3':
        View_Customer_Transaction()
    elif otheraction == '5':
        Cstatementofaccountreport()
    elif otheraction == '6':
        login()
    else:
        print("Invalid action.")
        admin()


def Cstatementofaccountreport():
    print("\n")
    print("=" * 100)
    print("***Customer's Statement Of Account Report***")
    print("=" * 100)
    print("\n")
    with open("transInfo.txt", "r") as fh:
        print("=" * 125)
        print("Date range of".ljust(20) + "|" + "Transaction Date".ljust(20) + "|" + "Account Balance".ljust(20) + "|" + "Account Type(s/c)".ljust(20) + "|" + "Email address".ljust(20) + "|" + "currency")
        print("=" * 125)
        for rec in fh:
            reclist = rec.strip("\n").split(":")
            print(reclist[0].ljust(20) + "|" + reclist[1].ljust(20) + "|" + reclist[2].ljust(20) + "|" + reclist[3].ljust(20) + "|" + reclist[4].ljust(20) + "|" + reclist[5], "\n")
        print("Do you want to perform other action(1/2/3/4/6)?")
        otheraction = input("")
        if otheraction == '1':
            Customeronboarding()
        elif otheraction == '2':
            View_Customer_Details()
        elif otheraction == '3':
            View_Customer_Transaction()
        elif otheraction == '4':
            Create_admin_Account()
        elif otheraction == '6':
            login()
        else:
            print("Invalid action.")
            admin()





def deposit():
    customer_transaction_data = []
    print("\t***DEOPSIT***\n")
    Userid = input("Please reenter ID for conformation: ")
    flg = "0"
    with open("transaction.txt", 'r+') as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if Userid == reclist[0]:
                flg = reclist
                break
        if flg == "0":
            print("Access Denied. Invalid LoginID.")
            deposit()
        else:
            print("\nWelcome! Do you wish to continue?\n Enter '5' to continue, any other number to Terminate: ")
            cont = input("")
            while cont != '5':
                print("Have a nice day")
                login()
            else:
                while True:
                    print("current balance is: RM", int(reclist[5]))
                    import datetime
                    date_day = datetime.datetime.now().strftime("%Y%m%d")
                    transactiontype = "D"
                    accounttype = input("Please enter account type: (S/C)")
                    depositamt = int(input("Please enter the amount you want to deposit: RM"))
                    availBal = int(reclist[5])
                    if depositamt <= 0:
                        print("deposit amount must be greater than RM0.")
                        break
                        deposit()
                    else:
                        newbl = depositamt + availBal
                        print("Your current balance is: RM", newbl)
                        rec = Userid + ":" + str(date_day) + ":" + transactiontype + ":" + str(
                            depositamt) + ":" + accounttype + ":" + str(newbl) + "\n"
                        customer_transaction_data.append(rec)
                        fh.write(str(customer_transaction_data))
                        fh.close()
                        print("\nTransaction performed successfully")
                        print("current balance is: RM", newbl)
                        print("Do you want to perform other action(2/3/4)?")
                        otheraction = input("")
                        if otheraction == '2':
                            Withdraw()
                        elif otheraction == '3':
                            reset_password()
                        elif otheraction == '4':
                            login()
                            break
                        else:
                            print("Invalid action.")
                            deposit()
        return flg




def Withdraw():
    print("***WITHDRAW***")
    customer_transaction_data = []
    Userid = input("Please reenter ID for conformation: ")
    flg = "0"
    with open("transaction.txt", 'r+') as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if Userid == reclist[0]:
                flg = reclist
                break
        if flg == "0":
            print("Access Denied. Invalid LoginID.")
            Withdraw()
        else:
            print("\nWelcome! Do you wish to continue?\n Enter '5' to continue, any other number to Terminate: ")
            cont = input("")
            while cont != '5':
                print("Have a nice day")
                login()
            else:
                while True:
                    print("current balance is: RM", int(reclist[5]))
                    import datetime
                    date_day = datetime.datetime.now().strftime("%Y%m%d")
                    transactiontype = "W"
                    accounttype = input("Please enter account type: (S/C)")
                    availBal = int(reclist[5])
                    withdraw = int(input("Please enter the amount you want to withdraw: RM"))
                    if withdraw > availBal:
                        print("Withdrawal amount exceeded account balance.")
                        Withdraw()
                    elif withdraw <= 0:
                        print("Invalid withdrawal amount")
                        Withdraw()
                    else:
                        newbl = availBal - withdraw
                        if accounttype == 'S':
                            mini_bal = 100
                            if newbl < mini_bal:
                                print("Transaction is not permitted, available balance for saving account must be at least RM100and for current account must be at least RM500")
                            else:
                                rec_1 = Userid + ":" + str(date_day) + ":" + transactiontype + ":" + str(
                                    withdraw) + ":" + accounttype + ":" + str(newbl)
                                customer_transaction_data.append(rec_1)
                                fh.write(str(customer_transaction_data))
                                fh.close()
                                print("\nTransaction performed successfully")
                                print("current balance is: RM", newbl)
                                print("Do you want to perform other action(1/3/4)?")
                                otheraction = input("")
                                if otheraction == '1':
                                    deposit()
                                elif otheraction == '3':
                                    reset_password()
                                elif otheraction == '4':
                                    break
                                else:
                                    print("Invalid action.")
                                    Withdraw()
                        else:
                            mini_bal2 = 500
                            if newbl < mini_bal2:
                                print("Transaction is not permitted, available balance for saving account must be at least RM100and for current account must be at least RM500")
                            else:
                                rec_2 = Userid + ":" + str(date_day) + ":" + transactiontype + ":" + str(
                                    withdraw) + ":" + accounttype + ":" + str(newbl)
                                customer_transaction_data.append(rec_2)
                                fh.write(str(customer_transaction_data))
                                fh.close()
                                print("\nTransaction performed successfully")
                                print("current balance is: RM", newbl)
                                print("Do you want to perform other action(1/3/4)?")
                                otheraction = input("")
                                if otheraction == '1':
                                    deposit()
                                elif otheraction == '3':
                                    reset_password()
                                elif otheraction == '4':
                                    break
                                else:
                                    print("Invalid action.")
                                    Withdraw()
        return flg


def reset_password():
    print("\n\t\t***RESET PASSWORD***\n")
    email_address = input("Please enter your email address: ")
    flg = "0"
    with open("custdetails.txt", 'r') as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if email_address == reclist[6]:
                flg = reclist
                break
        if flg == "0":
            print("Access Denied. Invalid Email address.")
            reset_password()
        else:
            print("\nWelcome! Do you wish to continue?\n Enter '5' to continue, any other number to Terminate: ")
            cont = input("")
            while cont != '5':
                print("Have a nice day")
                login()
            else:
                while True:
                  print("please enter your new password: ")
                  newpw = input("")
                  print("please reenter your new password for conformation: ")
                  confpw = input("")
                  if newpw != confpw:
                    print("Your new and confirm password do not match.")
                    reset_password()
                  else:
                    with open("newpw.txt","a") as fh1:
                      customer_transaction_data = []
                      customer_transaction_data.append(email_address)
                      customer_transaction_data.append(newpw)
                      fh1.write(str(customer_transaction_data))
                      fh1.close()
                      print("\nYour password has changed!")
                      print("Do you want to perform other action(1/2/4)?")
                      otheraction = input("")
                      if otheraction == '1':
                        deposit()
                      elif otheraction == '2':
                        Withdraw()
                      elif otheraction == '4':
                        login()
                      else:
                        print("Invalid action.")
                        reset_password()
        return flg






















login()
admin()
Customerlogin()
Customeronboarding()
View_Customer_Details()
View_Customer_Transaction()
Create_admin_Account()
reset_password()
Withdraw()
Cstatementofaccountreport()
deposit()
reset_password()

