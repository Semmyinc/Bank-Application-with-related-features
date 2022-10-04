# import pymysql
# from curses.ascii import isdigit
import re
# import random
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# database = {}
# class Gtbank:
#     def __init__(self):
#         self.balance = 0
#         # self.pin = int(input('Pin: '))
#         # self.account_number = 0
#         self.database = {}

#     def welcome(self):
#         print(f'Welcome to GTCO\nEnter 1 to Register or 2 to Login')
#         self.choice = int(input('Response: '))
#         if self.choice == 1:
#             g.registration()
            
#         elif self.choice == 2:
#             g.login()
#         else:
#             print(f'Invalid input!\nSelect between options 1 and 2 to proceed.')
    
#     def login(self):    
#         print(f'Login below...')
#         # self.balance = 0
#         self.email = input('Email: ')
#         self.pword = input('Password: ')
#         if self.email == self.database['self.email'] and self.pword == self.database['self.pword']:
#             g.menu()
#         else:
#             print('Incorrect Email or Password')
#             quit()

#     def registration(self):

#         print(f'Register below...')
#         # self.balance = 0
#         self.fname = input('Firstname: ').upper()
#         self.sname = input('Surname: ').upper()
#         self.uname = input('Username: ').lower()
#         self.phone = input('Phone Number: ')
#         if len(self.phone) == 11 and re.match('^[0-9]*$', self.phone):
#             print(f'Valid Phone Number')
#         else:
#             print(f'Invalid Phone Number')
#             quit()
#         self.email = input('Email: ')
#         if(re.fullmatch(regex, self.email)):
#             print("Valid Email")
#             self.pword = input('Password: ')
#             self.conf_pword = input('Confirm Password: ')
#             if self.conf_pword != self.pword:
#                 print(f'Password Mis-match!\nTry again')
#                 quit()
#             else:  
#                 print(f'Password confirmed successfully.\nEnter Pin')          
#                 self.pin = int(input('Pin: '))
#                 self.conf_pin = int(input('Confirm Pin: '))
#                 if self.conf_pin != self.pin:
#                     print(f'Pin Mis-match!\nTry again')
#                     quit()
#                 else:  
#                     print(f'Pin confirmed successfully.')
#                     self.account_number = random.randrange(1111111111, 2222222222)   
#                     print(f'Welcome onboard {self.fname}!\nYour Account Number is {self.account_number}\nPlease Login to fund your account and execute transactions.')
#                     self.database['self.fname'] = self.fname
#                     self.database['self.sname'] = self.sname
#                     self.database['self.uname'] = self.uname
#                     self.database['self.phone'] = self.phone
#                     self.database['self.email'] = self.email
#                     self.database['self.pword'] = self.pword
#                     self.database['self.conf_pword'] = self.conf_pword
#                     self.database['self.pin'] = self.pin
#                     self.database['self.conf_pin'] = self.conf_pin
#                     self.database['self.balance'] = self.balance
#                     self.database['self.account_number'] = self.account_number
#                     print(self.database)
#                     g.login()

            
#         else:
#             print("Invalid Email")
#             quit()     

#     def login(self):    
#         print(f'Login below...')
#         # self.balance = 0
#         self.email = input('Email: ')
#         self.pword = input('Password: ')
#         if self.email == self.database['self.email'] and self.pword == self.database['self.pword']:
#             g.menu()
#         else:
#             print('Incorrect Email or Password')
#             quit()

#     def menu(self):
        
#         print('''
#             1. Check Balance
#             2. Deposit
#             3. Withdrawal/Transfer
#             4. Purchase Airtime/Data
#             5. Confirm cheque
#             6. Speak with a customer service representative.

#             ''')
#         choice = int(input('Response: '))

#         # Check Balance
#         if choice == 1:
#             self.pin2 = int(input('Pin: '))
#             if self.pin2 == self.database["self.pin"]:
#                 print(f'Available Balance is {self.database["self.balance"]}')
        
#         # Deposit
#         elif choice == 2:
#             self.pin = int(input('Pin: '))
#             deposit_amount = float(input('Deposit Amount: '))
#             self.balance += deposit_amount
#             self.database['self.balance'] = self.balance
#             print(f'Deposit Successful\nNew Available Balance is {self.database.get("self.balance")}')
            

# g = Gtbank()
# g.welcome()
phone = '+2347035151269'
phone0 = '2347035151269'
phone1 = '08035151269'
phone2 = '08160811821'
phone3 = '07060811821'
phone4 = '07030811821'
phone5 = '08060811821'
phone6 = '08130811821'
phone7 = '08140811821'
phone8 = '08100811821'
phone4 = '09030811821'
phone4 = '09060811821'
phone11 = '09152270643'
phone3 = '08037694921'
land_line = '0904614000'
mtn = ['0703', '+234703', '0706', '+234706', '0803', '+234803', '0806', '+234806', '0813', '+234813', '0814', '+234814', '0810', '+234810', '0816', '+234816', '0903', '+234903', '0906', '+234906']
glo = ['0705', '+234705', '0805', '+234805', '0807', '+234807', '0811', '+234811', '0815', '+234815', '0905', '+234905']
ninemobile = ['0809', '+234809', '0817', '+234817', '0818', '+234818', '0908', '+234908', '0909', '+234909']
airtel = ['0802', '+234802', '0808', '+234808', '0812', '+234812', '0708', '+234708', '0701', '+234701', '0902', '+234902', '0901', '+234901', '0907', '+234907']
nitel = ['01', '+23401', '02', '+23402', '03', '+23403', '04', '+23404', '05', '+23405', '06', '+23406', '07', '+23407', '08', '+23408', '09', '+23409']
# ninemobile = ['']
# regex_phone = r'(^\+)(234){1}[0-9]{10}'
# regex_phone1 = r'(^234)[0-9]{10}'
# regex_phone2 = r'^0[7|8|9]{1}[0-9]{9}'
# regex_phone3 = r'^0(7|8|9){1}(0|1){1}[0-9]{8}'
# regex_land1 = r'^0[1-9]{1}[1-9]{8}'
# regex_land2 = r'^+(234){1}[1-9]{1}[0-9]{8}'
# regex_combined = r'((^\+)(234){1}[0-9]{10})|(^0(7|8|9){1}(0|1){1}[0-9]{8})|((^234)[0-9]{10})'

# mtn = r'(^0[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[0|3|4|6]{1}[0-9]{7})'
# glo = r'(^0[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[1|5|7]{1}[0-9]{7})'
# ninemobile = r'(^0[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})|(^\+(234){1}[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})|(^234[8|9]{1}[0|1]{1}[7|8|9]{1}[0-9]{7})'
# airtel = r'(^0[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})|(^\+(234){1}[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})|(^234[7|8|9]{1}[0|1]{1}[1|2|7|8]{1}[0-9]{7})'
# nitel = r'(^0[1-9]{1}[0-9]{8})|(^\+(234)[0-9]{8})|(^234[0-9]{8})'
# # if re.search(regex_phone, phone1):
# if re.fullmatch(glo, phone11):
#     print('glo')
# else:
#     print('Invalid')
# phone11 = '0818081182'
# phone11 = '+234818081182'
# phone11 = '+2348180811821'
phone11 = '2348180811821'
# phone11 = '08180811821'
# print(len(phone12))

# print(phone12[:7])
if phone11[:4] in mtn and len(phone11) == 11:
    print('mtn')

# # elif phone11[:4] in glo:
# #     print('glo')
elif phone11[:4] in ninemobile and len(phone11)  == 11 or phone11[:7] in ninemobile and len(phone11) == 14 or phone11[:6] in ninemobile and len(phone11) == 13:
    print('9mobile')
# elif phone11[:7] in ninemobile and len(phone11) == 14:
#     print('9mobile')
# elif phone11[:6] in ninemobile and len(phone11) == 13:

#     print('9mobile')
# elif phone11[:4] in airtel:
#     print('Airtel')
# # elif phone11[:4] in nitel:
# #     print('Nitel')
# else:
#     print('Invalid Phone Number')