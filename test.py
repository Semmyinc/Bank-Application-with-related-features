self.fname = input('Firstname: ').upper()
self.sname = input('Surname: ').upper()
self.uname = input('Username: ').lower()
self.phone = input('Phone Number: ')
if re.fullmatch(mtn, self.phone):
    print('MTN')
elif re.fullmatch(glo, self.phone):
    print('GLO')      
elif re.fullmatch(ninemobile, self.phone):
    print('9mobile')
elif re.fullmatch(airtel, self.phone):
    print('AIRTEL')
elif re.fullmatch(nitel, self.phone):
    print('NITEL')
else:
    print('Invalid Phone Number. Try again.')