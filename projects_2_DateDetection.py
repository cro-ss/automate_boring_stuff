## Date detection
dates = '''12/12/2025
15/06/2025
05/06/1999
30/05/2001
29/12/2025
28/13/2025
12/06/3001
31/06/2025
31/04/2025
31/09/2023
30/02/2025
28/02/2100
29/02/2004
29/02/2008
29/02/2003
31/02/2004
28/02/2023
29/02/2100'''
# Empty list day, month, year and whole dates
day=[]
month=[]
year=[]
valid_dates=[]
# The regex of day,month , year
import re
date= re.compile(r'''(0[1-9]|[12][0-9]|3[01])
                    /
                    (0[1-9]|1[0-2])
                    /
                    (1\d{3}|2\d{3})''',re.VERBOSE)
# I am gathering each part of a date in their regarding list
for groups in date.findall(dates):
    day.append(groups[0])
    month.append(groups[1])
    year.append(groups[2])
#Here I am defining the constraints of the day, year and so on, leap year, 30,31 or 28 days per month
for i in range(len(day)):
    if year[i]<'1000' or year[i]>'2999':
        print(i,' year not valid')
    elif(month[i]== '04' or month[i]== '06' or month[i]== '09') and (day[i]>'30'):
           print(day[i], '/', month[i],'are not valid dates')
    elif month[i]=='02' and day[i]>'29':
        print(day[i], '/', month[i],'/',year[i],'are not valid dates')
    elif month[i]=='02' and (int(year[i])%4!=0 or int(year[i])%100==0) and int(year[i])%400!=0  and (day[i]>'28'):
          print(day[i], '/', month[i],'/',year[i],'are not valid dates')
    else:
        valid_dates.append(day[i]+ '/'+month[i]+'/'+ year[i])
        list_dates='\n'.join(valid_dates)
print('Valid dates:\n',list_dates)



