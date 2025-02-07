from datetime import datetime

birthdate=input("Your birthdate (DD/MM/YYYY):")
date=datetime.strptime(birthdate, "%d/%m/%Y")

x= datetime.now()


age_year=x.year - date.year
age_month=x.month - date.month
age_day=x.day - date.day
age=age_year
if age_month <0:
    age=age_year-1
else :
    if age_day <0 and date.month==x.month:
        age=age_year-1

print(age)


candle=age%10
candles="i"*candle
birthcake=f"""
   ___{candles}___
  |:H:a:p:p:y:|
__|___________|__
|^^^^^^^^^^^^^^^^|
|B:i:r:t:h:d:a:y:|
|                |
~~~~~~~~~~~~~~~~~~
"""

if date.year %4 ==0:
    print(birthcake * 2)
else :
    print(birthcake)
