def leap_year(year):
	return ( (year%400 == 0) or ( (year%100 !=0) and (year%4 ==0)) )

def last_day(month,year):
	if month ==2:
		if(leap_year(year)):
			ld=29
		else:
			ld=28

	elif month in (4,6,9,11):
		ld=30

	else:
		ld=31

	return ld
	
'''
pre-conditions : 
	day is a positive 1 or 2 digit number between 1 and 31
	month is a positive 1 or 2 digit number between 1 and 12
	year is a positive 4 digit number between 1800 and 2018

post-condition : return a list date=[day,month,year] reflecting the next date
'''
			
def nextDate(day,month,year):
	
	if day==31 and month == 12:
		day=1
		month=1
		year+=1

	elif day == last_day(month,year):
		day=1
		month +=1
		
	elif day >=1 and day < last_day(month,year):
		day +=1
		
	else :
		print('impossible date')
		exit()

	return [str(day),str(month),str(year)]
	

day=int(input('enter day '))
if day<1 or day>31:
	print('Invalid input.Ensure 1<=day<=31')
	exit()

month=int(input('enter month '))
if month<1 or month>12:
	print('Invalid input.Ensure 1<=month<=12')
	exit()

year=int(input('enter year '))
if year<1800 or year>2018:
	print('Invalid input.Ensure 1800<=year<=2018')
	exit()

#since date satisfies the preconditions call the nextDate function
date=(nextDate(day,month,year))
print('/'.join(date))
