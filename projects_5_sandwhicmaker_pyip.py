# Escribe tu código aquí :-)
import pprint


import pyinputplus as pyip
bread={'wheat': 2.0, 'white': 1.75, 'sourdough':2.25}
protein={'chicken':3.0,'turkey':3.25,'ham':2.5,'tofu':4.0}
cheese={'cheddar': 1.5, 'swiss':2.0,'mozzarella':1.75}
sandwiche_price= 0
prepared_sandwich=[]
while True:
        #asking for bread
    response = pyip.inputMenu(['wheat','white','sourdough'])
    print('You have chosen %s'% response)
    price=bread[response]
    prepared_sandwich.append(response)
    print('The price is %s' % price)
        #asking for protein
    response = pyip.inputMenu(['chicken','turkey','ham','tofu'])
    price = price + protein[response]
    prepared_sandwich.append(response)
    print('The price is %s' % price)
    response_1= pyip.inputYesNo('Do you want cheese? \n')
    if response_1 == 'yes' :
        #asking for cheese
        response=pyip.inputMenu(['cheddar','swiss','mozarella'])
        price= price+ cheese[response]
        prepared_sandwich.append(response)
        print('The price is %s' % price)
    response_1= pyip.inputYesNo('Do you want mayo? \n')
    if response_1 == 'yes':
        prepared_sandwich.append('mayo')
    response_1= pyip.inputYesNo('Do you want mustard? \n')
    if response_1 == 'yes':
        prepared_sandwich.append('mustard')

    response_1= pyip.inputYesNo('Do you want lettuce? \n')
    if response_1 == 'yes':
        prepared_sandwich.append('letucce')

    response_1= pyip.inputYesNo('Do you want tomatoe?\n')
    if response_1 == 'yes':
        prepared_sandwich.append('tomatoe')

    response= pyip.inputInt('How many sandwhices do you want: \n')
    price = price*response
    break
print(f'Your bill is:{price} Thank you for comming')

pprint.pprint(prepared_sandwich)




