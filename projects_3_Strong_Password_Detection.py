# Project 2
# Strong Password Detection
#step 1 def the function
import re
def strongpassword(password):
#step 2 defining the refex: letters, special symbols, numbers and Uppercase
#At least 8 characters
    regex_password= re.compile(r'[a-zA-Z0-9+-@]{8,}')
    result=regex_password.search(password)
    test=result.group()
    print(result) #Print your written password
    print(result.group())

    regex_digit=re.compile(r'\d+') #Rex that evaluates one digit
    mo1=regex_digit.search(test)
    if mo1== None:
        print('you need at least one digit')

    regex_upper= re.compile(r'[A-Z]+') #Regex that evaluates Uppercase
    mo2=regex_upper.search(test)
    if mo2== None:
        print('you need at least one uppercase')


    regex_lowe = re.compile(r'[a-z]+')#Regex that evaluates lowecase
    mo3=regex_lowe.search(test)
    if mo3== None:
        print('you need at least one lowecase')


    regex_symbol= re.compile(r'[@+-]+') #Regex that evaluates extrasymbols
    mo4=regex_symbol.search(test)
    if mo4== None:
        print('you need at least one symbol')

    if mo1 != None and mo2 != None and mo3!= None and mo4 != None: #conditions that evaluates if the password fullfills all the constraints
        print('Your password:',key, 'is valid')
        exit_1 = 1
        return True
    else:
        return False
##Loop that runs until the password fullfills all the statements
while True:
    print('Ingrese su contraseña: ')
    key = input()
    if strongpassword(key):
        break
