
import pymysql
import re
import random
import maskpass

# Email Validator 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Local Nigerian phone number validity checker by service providers- Regex Metthod(95% accuracy)
mtn = r'(^0[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})'
glo = r'(^0[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})'
ninemobile = r'(^0[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})|(^\+(234){1}[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})|(^234[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})'
airtel = r'(^0[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})'
nitel = r'(^0[1-9]{1}[0-9]{8})|(^\+(234)[0-9]{8})|(^234[0-9]{8})'

# Bank Verification Number (BVN) generator - Regex method (100% accuracy)
bvn = r'^2[2]{1}[2|3|4]{1}[0-9]{8}'

# Local Nigerian phone number validity checker by service providers - List Method(100% accuracy)
mtnn = ['0703', '+234703', '0706', '+234706', '0803', '+234803', '0806', '+234806', '0813', '+234813', '0814', '+234814', '0810', '+234810', '0816', '+234816', '0903', '+234903', '0906', '+234906']
gloo = ['0705', '+234705', '0805', '+234805', '0807', '+234807', '0811', '+234811', '0815', '+234815', '0905', '+234905']
ninemobilee = ['0809', '+234809', '0817', '+234817', '0818', '+234818', '0908', '+234908', '0909', '+234909']
airtell = ['0802', '+234802', '0808', '+234808', '0812', '+234812', '0708', '+234708', '0701', '+234701', '0902', '+234902', '0901', '+234901', '0907', '+234907']
nitell = ['01', '+23401', '02', '+23402', '03', '+23403', '04', '+23404', '05', '+23405', '06', '+23406', '07', '+23407', '08', '+23408', '09', '+23409']


# Database
server = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='Project')
move = server.cursor()
# move.execute('CREATE DATABASE Project')
# move.execute('SHOW DATABASES')
# for database in move:
#     print(database)

# move.execute('CREATE TABLE Access_bank (Cust_Id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, Firstname VARCHAR(20) NOT NULL, Surname VARCHAR(20) NOT NULL, Username VARCHAR(20) NOT NULL, Phone INT(11) NOT NULL, Email VARCHAR(30) NOT NULL, Password VARCHAR(20) NOT NULL, Confirm_Password VARCHAR(20) NOT NULL, Pin INT(4) NOT NULL, Confirm_Pin INT(4) NOT NULL, Balance INT(20) NOT NULL, Account_Number INT(10) NOT NULL)')
# move.execute('SHOW TABLES')
# for table in move:
#     print(table)

# move.execute("CREATE TABLE Access_Bank (ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT NOT NULL, Firstname VARCHAR(20) NOT NULL, Surname VARCHAR(20) NOT NULL, Username VARCHAR(20) NOT NULL, Phone VARCHAR(11) UNIQUE NOT NULL, Network VARCHAR(11) NOT NULL, Airtime VARCHAR(11) NOT NULL, Data VARCHAR(11) NOT NULL, Email VARCHAR (30) UNIQUE NOT NULL, Password VARCHAR(20) NOT NULL, Confirm_Password VARCHAR(20) NOT NULL, Pin VARCHAR(4) NOT NULL, Confirm_Pin VARCHAR(4) NOT NULL, Balance VARCHAR (20) NOT NULL, Account_Number VARCHAR(10) UNIQUE NOT NULL)")
# move.execute("SHOW TABLES")
# for table in move: 
#     print(table)

# move.execute("CREATE TABLE Phone_Schedule (ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT NOT NULL, Firstname VARCHAR(20) NOT NULL, Surname VARCHAR(20) NOT NULL, Username VARCHAR(20) NOT NULL, Phone VARCHAR(11) NOT NULL, Network VARCHAR (7) NOT NULL, Airtime_Bal VARCHAR(20) NOT NULL, Pin INT(4) NOT NULL, Account_Number INT(10) NOT NULL)")
# move.execute("SHOW TABLES")
# for table in move: 
#     print(table)
class Access_Bank:
    def __init__(self):
        self.balance = 0
        self.airtime = 0
        self.data = 0
        self.schedule = ()
        # self.pin = int(input('Pin: '))
        # self.account_number = 0
    
    # Welcome Message
    def welcome(self):
        self.choicecount = 1

        print(f'Welcome to Access Bank Plc.')
        while self.choicecount <= 3:
            print('Enter 1 to Register or 2 to Login')
            self.choice = int(input('Response: '))
            if self.choice == 1:
                a.registration()
                break
            elif self.choice == 2:
                a.login()
                break
            else:
                print(f'Invalid input!\nSelect between options 1 and 2 to proceed.')
                self.choicecount += 1
    
    # User registration
    def registration(self):
        self.phonecount = 1
        self.emailcount = 1
        self.confpwordcount = 1
        self.confpincount = 1
        self.bvncount = 1
        print(f'Register below...')
        # self.balance = 0
        self.fname = input('Firstname: ').upper()
        self.sname = input('Surname: ').upper()
        self.uname = input('Username: ').lower()
        # self.phone = input('Phone Number: ')
        while self.phonecount <= 3:
            self.phone = input('Phone Number: ')
            if self.phone[:4] in mtnn and len(self.phone) == 11 or self.phone[:7] in mtnn and len(self.phone) == 14:
            # if re.fullmatch(mtn, self.phone):
                print('MTN')
                break
            elif self.phone[:4] in gloo and len(self.phone) == 11 or self.phone[:7] in gloo and len(self.phone) == 14:
                print('GLO')      
                break
            elif self.phone[:4] in ninemobilee and len(self.phone) == 11 or self.phone[:7] in ninemobilee and len(self.phone) == 14:
                print('9mobile')
                break
            elif self.phone[:4] in airtell and len(self.phone) == 11 or self.phone[:7] in airtell and len(self.phone) == 14:
                print('AIRTEL')
                break
            elif self.phone[:4] in nitell and len(self.phone) == 11 or self.phone[:7] in nitell and len(self.phone) == 14:
                print('NITEL')
                break
            else:
                print('Invalid Phone Number.\nTry again.')
                self.phonecount += 1 
        else:
            print('Valid Phone input tries execeeded. Try again later')
            quit()
        
        while self.emailcount <= 3:
            self.email = input('Email: ').lower()
            if(re.fullmatch(regex, self.email)):
                print("Valid Email")
                break
            else:
                print('Invalid Email\nTry again.')
                self.emailcount += 1
        else:
            print('Email input trial attempts exhausted.\nTry again later ')
            quit()
       
        self.pword = maskpass.askpass(prompt = 'Password: ', mask = '*')
       
        while self.confpwordcount <= 3:
            self.conf_pword = maskpass.askpass(prompt = 'Confirm Password: ', mask = '*')
            if self.conf_pword != self.pword:
                print(f'Password Mis-match!\nTry again')
                self.confpwordcount += 1
            else:  
                print(f'Password confirmed successfully.\nEnter Pin')
                break  
        else:
            print('Password Confirmation chances exhausted.\nTry again later.')   
            quit()     
        
        self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
        while self.confpincount <= 3:
            self.conf_pin = int(maskpass.askpass(prompt = 'Confirm Pin: ', mask = '*'))
            if self.conf_pin != self.pin:
                print(f'Pin Mis-match!\nTry again')
                self.confpincount += 1
            else: 
                print(f'Pin confirmed successfully.')
                break
        else:
            print('Password Confirmation chances exhausted.\nTry again later.') 
            quit()
       
        self.account_number = int(random.randrange(3333333333, 4444444444))   
        print('Have BVN? (Y/N)')
        choice = input('Response: ').upper()
        if choice == 'Y':
            print('Enter the number below')
            while self.bvncount <= 3:
                self.bvn = input('BVN: ')
                if re.fullmatch(bvn, self.bvn):
                    print('Valid BVN')
                    break
                else:
                    print('Invalid Biometric Number.\nTry again.')
                    self.bvncount += 1
            else:
                print('You have run out of chances for BVN trials\nTry again much later.')
                quit()
        else:
            print('BVN is required to complete this registration process.\nEnter 1 to Enroll for BVN or 2 to Quit this process.')
            bvnchoice = int(input('Response: '))
            if bvnchoice == 1:
                print('BVN Enrolling ongoing...')
                self.bvn = random.randrange(22222222222, 22499999999)
                print(f'Your Biometric Verification Number (BVN) is {self.bvn}')
            elif bvnchoice == 2:
                print('Thank you for your interest in Access Bank.\nWe do hope you would check again soon.')
                quit() 
        record = "INSERT INTO Access_Bank (Firstname, Surname, Username, Phone, BVN, Airtime, Data, Email, Password, Confirm_Password, Pin, Confirm_Pin, Balance, Account_Number) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.fname, self.sname, self.uname, self.phone, self.bvn, self.airtime, self.data, self.email, self.pword, self.conf_pword, self.pin, self.conf_pin, self.balance, self.account_number)
        move.execute(record, val)
        # mycursor.executemany((myquery, val),())
        server.commit()
        print(move.rowcount, "records inserted successfully")
        print(f'Welcome onboard {self.fname}!\nYour Account Number is {self.account_number}\nPlease Login to fund your account and execute transactions.')
        # schedule = move.fetchone()
        # print(schedule)
        a.login()
        
    # User Login
    def login(self): 
        self.logincount = 1
        while self.logincount <= 3:
            print(f'Login below...')
        # self.balance = 0
            self.email = input('Email: ')
            # masking password
            self.pword = maskpass.askpass(prompt = 'Password: ', mask = '*')
            recordlogin = "SELECT * FROM Access_bank WHERE Email = %s AND Password = %s"
            val = (self.email, self.pword)
            move.execute(recordlogin,val)
            self.schedule = move.fetchone()
            # print(self.schedule)
            if self.email != self.schedule[8] and self.pword != self.schedule[-5]:
                print(f'Incorrect Email or Password')
                self.logincount += 1
                # print(f'You have {self.logincount} attempt(s) left')
            # elif self.email == self.schedule[8] or self.pword != self.schedule[-5]:
            #     print(f'correct Email and wrong Password')
            # elif self.email != self.schedule[8] or self.pword == self.schedule[-5]:
            #     print(f'incorrect Email and correct Password')
            else:
                a.menu()
                break
        else:
            print('Login attempts failed consecutively\nYou have been locked out.\nContact our Customer Representatives to unlock your account')

    # Link Function
    def ask(self):
        count = 1
        print(f'Would you like to perform other transactions? (Y/N)')
        while count <= 3:
            ask = input("Response: ").upper()
            if ask == 'Y':
                a.menu()
            elif ask == 'N':
                print(f'Thank you for banking with us.\nHave a nice day.')
                quit()
            else:
                print('Invalid Input.\nEnter Y for Yes and N for No to proceed')
                count += 1        
        else:
            print('You keep prompting me with wrong input\nYou should watch it or get the hell out of here!lol!')
    
    # Transactions
    def menu(self):
        print('''
            1. Check Balance
            2. Deposit
            3. Withdrawal/Transfer
            4. Purchase Airtime/Data
            5. Speak with a customer service representative.
            
            ''')
        choice = int(input('Response: '))

        # Check Balance
        if choice == 1:
            self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
            # record = "SELECT * FROM access_bank WHERE Pin = %s"
            # val = (self.pin)
            # move.execute(record,val)
            # self.schedule = move.fetchone()
            # print(schedule)
            if self.pin == self.schedule[-3]:
                print(f'Name: {self.schedule[1]} {self.schedule[2]}, Available Balance: {self.schedule[-2]}')
                a.ask()
            else:
                print('Incorrect Pin')
                a.ask()
        
        
        # Deposit
        elif choice == 2:
            self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
            # record = "SELECT * FROM access_bank WHERE Pin=%s"
            # val =(self.pin)
            # move.execute(record, val)
            # schedule = move.fetchone()
            self.accessbal = float(self.schedule[-2])
            deposit_amount = float(input('Deposit Amount: '))
            self.balance = self.accessbal + deposit_amount
            # self.balance = self.uname
            record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
            val =(self.balance, self.pin)
            move.execute(record, val)
            server.commit()
            # print(move.rowcount, 'record updated successfuly')
            print(f'Deposit executed successfully\nYour Available Balance is {self.balance}.')          
            a.ask()

        
        # Withdrawal/Transfer
        elif choice == 3:
            self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
            # withdraw_amount = float(input('Deposit Amount: '))
            # self.balance -= withdraw_amount
            # record = "SELECT * FROM access_bank WHERE Pin=%s"
            # val =(self.pin)
            # move.execute(record, val)
            # schedule = move.fetchone()
            
            if self.pin == self.schedule[-3]:
                transfer_amount = float(input('Amount to Transfer: '))
                transfer_charge = 57.25
                total_transfer_amount = transfer_amount + transfer_charge
                self.balance = float(self.schedule[-2])
                    
                if total_transfer_amount <= self.balance:
                    print(f'1. Transfer within Access Bank\n2. Transfer to Other Banks.')
                    choice = int(input('Response: '))

                    # Intra-Bank Transfer - Access
                    if choice == 1:
                        beneficiary_account_no = int(input('Beneficiary Account Number: '))
                        record = "SELECT * FROM access_bank WHERE Account_Number=%s"
                        val =(beneficiary_account_no)
                        move.execute(record, val)
                        schedule = move.fetchone()
                        # print(schedule)
                        self.accessbal = float(schedule[-2])
                        print(f'Name: {schedule[1]} {schedule[2]}, Access Bank')
                        # self.pin = int(input('Pin: '))
                        # record_user_access = "SELECT * FROM access_bank WHERE Pin=%s"
                        # val =(self.pin)
                        # move.execute(record_user_access, val)
                        # schedule_user_access = move.fetchone()
                            # print(schedule1)
                            # print(f'Name: {schedule1[1]} {schedule1[2]},gtbank')
                        if self.pin == self.schedule[-3]:
                            self.balance -= transfer_amount
                            self.newbalance = self.accessbal + transfer_amount
                            record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
                            record2 = "UPDATE access_bank SET Balance=%s WHERE Account_Number=%s"
                            val1 =(self.balance, self.pin)
                            val2 = (self.newbalance,beneficiary_account_no)
                            move.execute(record, val1)
                            move.execute(record2,val2)
                            server.commit()
                            # print(move.rowcount, 'record updated successfuly')
                            print(f'Transfer effected successfully\nYour Available Balance is {self.balance}.')
                            a.ask()
                        else:
                            print('Incorrect Pin!\nTry again.')
                            a.ask()

                    # Transfer to other banks
                    elif choice == 2:
                        print('Select Beneficiary Bank\n1. GTCO\n2. Polaris Bank')
                        beneficiary_bank = int(input('Beneficary Bank: '))
                        
                        # Transfer to other bank - GTCO
                        if beneficiary_bank == 1:
                            beneficiary_account_no = int(input('Beneficiary Account Number: '))
                            if beneficiary_account_no:
                                record = "SELECT * FROM gtbank WHERE Account_Number=%s"
                                val =(beneficiary_account_no)
                                move.execute(record, val)
                                schedule = move.fetchone()
                                # print(schedule)
                                self.gtcobal = float(schedule[-2])
                                print(f'Name: {schedule[1]} {schedule[2]}, GTCO')
                                # self.pin = int(input('Pin: '))
                                # record1 = "SELECT * FROM access_bank WHERE Pin=%s"
                                # val =(self.pin)
                                # move.execute(record1, val)
                                # schedule1 = move.fetchone()
                                # print(schedule1)
                                # print(f'Name: {schedule1[1]} {schedule1[2]},gtbank')
                                if self.pin == self.schedule[-3]:
                                    self.balance -= total_transfer_amount
                                    self.newbalance = self.gtcobal + transfer_amount
                                    record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
                                    record2 = "UPDATE gtbank SET Balance=%s WHERE Account_Number=%s"
                                    val1 =(self.balance, self.pin)
                                    val2 = (self.newbalance,beneficiary_account_no)
                                    move.execute(record, val1)
                                    move.execute(record2,val2)
                                    server.commit()
                                    # print(move.rowcount, 'record updated successfuly')
                                    print(f'Transfer effected successfully\nYour Available Balance is {self.balance}.')
                                    a.ask()
                                else:
                                    print('Incorrect Pin!\nTry again.')
                                    a.ask()
                            else:
                                print('Invalid Account Number')
                                a.ask()


                        # Transfer to other bank - Polaris Bank
                        elif beneficiary_bank == 2:
                            beneficiary_account_no = int(input('Beneficiary Account Number: '))
                            if beneficiary_account_no:
                                record = "SELECT * FROM Polaris_Bank WHERE Account_Number=%s"
                                val =(beneficiary_account_no)
                                move.execute(record, val)
                                schedule = move.fetchone()
                                # print(schedule)
                                polarisbal = float(schedule[-2])
                                print(f'Name: {schedule[1]} {schedule[2]}, Polaris Bank')
                                # self.pin = int(input('Pin: '))
                                # record = "SELECT * FROM access_bank WHERE Pin=%s"
                                # val =(self.pin)
                                # move.execute(record, val)
                                # schedule1 = move.fetchone()
                                # print(schedule1)
                                # print(f'Name: {schedule1[1]} {schedule1[2]},gtbank')
                                if self.pin == self.schedule[-3]:   
                                    self.balance -= total_transfer_amount 
                                    self.newbalance = polarisbal + transfer_amount                  
                                    record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
                                    record1 = "UPDATE polaris_bank SET Balance=%s WHERE Account_Number=%s"
                                    val1 =(self.balance, self.pin)
                                    val2 = (self.newbalance, beneficiary_account_no)
                                    move.execute(record, val1)
                                    move.execute(record1, val2)
                                    server.commit()
                                    # print(move.rowcount, 'record updated successfuly')
                                    print(f'Transfer effected successfully\nYour Available Balance is {self.balance}')
                                    a.ask()
                                else:
                                    print('Incorrect Pin!\nTry again.')
                                    a.ask()
                            else:
                                print('Invalid Account Number')
                                a.ask()
                        else:
                            print('Invalid Selection.\nChoose either 1 or 2 to continue.')
                            a.ask()
                else:
                    print(f'Insufficient Balance')
                    a.ask()
            else:
                print('Incorrect Pin')
                a.ask()

        #Bills Payment
        # Airtime Purchase
        elif choice == 4:
            print('Press 1 for Airtime or 2 for Data')
            selection = int(input('Response: '))
            if selection == 1:
               self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
            #    record = "SELECT * FROM access_bank WHERE Pin=%s"
            #    val =(self.pin)
            #    move.execute(record, val)
            #    schedule = move.fetchone()
               # print(schedule)
               print(f'Name: {self.schedule[1]} {self.schedule[2]} {self.schedule[-2]},  Access Bank')
               card_amount = float(input('Airtime Amount: ')) 
               self.balance = self.schedule[-2]
               if card_amount > self.balance:
                print('Insufficient Fund')
               else:
                phone_number = input('Phone Number: ')
                if re.fullmatch(mtn, phone_number):
                    print('MTN')
                elif re.fullmatch(glo, phone_number):
                    print('GLO')      
                elif re.fullmatch(ninemobile, phone_number):
                    print('9mobile')
                elif re.fullmatch(airtel, phone_number):
                    print('AIRTEL')
                elif re.fullmatch(nitel, phone_number):
                    print('NITEL')
                else:
                    print('Invalid Phone Number. Try again.')
                # print('1. MTN 2. Airtel 3. 9mobile 4. Glo')
                # network_provider = int(input('Network: '))
                # # if network_provider == 1 or network_provider == 2 or network_provider == 3 or network_provider == 4:
                # if network_provider == 1 or 2 or 3 or 4:
                record = "SELECT * FROM access_bank WHERE Phone=%s"
                
                val =(phone_number)
                move.execute(record, val)
                schedule = move.fetchone()
                # print(schedule)
                accessairtimebal = float(schedule[6])
                #    print(f'Name: {schedule[1]} {schedule[2]} {schedule[-2]},  GTCO')
                if self.pin == self.schedule[-3]:
                    self.balance -= card_amount
                    self.airtime = accessairtimebal + card_amount                   
                    record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
                    record1 = "UPDATE access_bank SET Airtime=%s WHERE Phone=%s"
                    val =(self.balance, self.pin)
                    val1 =(self.airtime, phone_number)
                    move.execute(record, val)
                    move.execute(record1, val1)
                    server.commit()
                    # print(move.rowcount, 'record updated successfuly')
                    print(f'Airtime Purchase successful.\nYour new balance is {self.balance}')
                    a.ask()
                else:
                        print('Incorrect Pin')
                        a.ask()
                # else:
                #     print('Invalid Input.\nSelect any of options 1 to 4 to proceed')
                #     a.ask()

            # Data Purchase    
            elif selection == 2:
                self.pin = int(maskpass.askpass(prompt = 'Pin: ', mask = '*'))
                # record = "SELECT * FROM access_bank WHERE Pin=%s"
                # val =(self.pin)
                # move.execute(record, val)
                # schedule = move.fetchone()
                # print(schedule)
                print(f'Name: {self.schedule[1]} {self.schedule[2]} {self.schedule[-2]},  Access Bank')
                data_amount = float(input('Data Amount: ')) 
                self.balance = float(self.schedule[-2])
                if data_amount > self.balance:
                    print('Insufficient Fund')
                    a.ask()
                else:
                    phone_number = input('Phone Number: ')
                    # print('1. MTN 2. Airtel 3. 9mobile 4. Glo')
                    # network_provider = int(input('Network: '))
                    # # if network_provider == 1 or network_provider == 2 or network_provider == 3 or network_provider == 4:
                    # if network_provider == 1 or 2 or 3 or 4:
                    if re.fullmatch(mtn, phone_number):
                        print('MTN')
                    elif re.fullmatch(glo, phone_number):
                        print('GLO')      
                    elif re.fullmatch(ninemobile, phone_number):
                        print('9mobile')
                    elif re.fullmatch(airtel, phone_number):
                        print('AIRTEL')
                    elif re.fullmatch(nitel, phone_number):
                        print('NITEL')
                    else:
                        print('Invalid Phone Number. Try again.')
                    record = "SELECT * FROM Access_Bank WHERE Phone=%s"
                    val =(phone_number)
                    move.execute(record, val)
                    schedule = move.fetchone()
                    accessdatabal = float(schedule[7])
                        # print(schedule)
                        #    print(f'Name: {schedule[1]} {schedule[2]} {schedule[-2]},  GTCO')
                    if self.pin == self.schedule[-3]:
                       self.balance -= data_amount
                       self.data = accessdatabal + data_amount
                       record = "UPDATE access_bank SET Balance=%s WHERE Pin=%s"
                       record1 = "UPDATE access_bank SET Data=%s WHERE Phone=%s"
                       val =(self.balance, self.pin)
                       val1 =(self.data, phone_number)
                       move.execute(record, val)
                       move.execute(record1, val1)
                       server.commit()
                       # print(move.rowcount, 'record updated successfuly')
                       print(f'Data Purchase successful.\nYour new balance is {self.balance}')
                       a.ask()
                    else:
                        print('Incorrect Pin')
                        a.ask()
                    # else:
                    #     print('Invalid Input.\nSelect any of options 1 to 4 to proceed')
                    #     a.ask()        
        
        # # Cheque Confirmation
        # elif choice == 5:
        #     print(f'Enter cheque details below')
        #     chq_no = int(input('Enter cheque number: '))
        #     issue_date = input('Enter date of issuance: ')
        #     ben_name = input('Enter Beneficiary Name: ')
        #     amt_on_chq = int(input('Enter Amount: '))
        #     a.ask()

        # Customer Sevice Representative
        elif choice == 5:
            print('Request to speak with customer service representative')
            print('connecting...')
            print('connecting...')
            print('connecting...')
            print('Hi there! My name is Susan. How may I help you?')
            a.ask()
        else:
            print(f'Invalid Input.\nSelect any of options 1 to 6 to proceed')
            a.ask()
a = Access_Bank()
# a.welcome()




