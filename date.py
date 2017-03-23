from datetime import date, time, timedelta, datetime
dt = datetime.now()
dt.strftime('%Y-%m-%d')
delta = timedelta (days = 1)
yesterday = dt - delta
yesterday.strftime('%Y-%m-%d')
def last_month():
	dt = datetime.now()
	if dt.month == 1 :
		delta = timedelta (days = 31)
		last_month = dt - delta
	else:
		last_month = dt.replace(month = dt.month-1)
	return last_month.strftime('%Y-%m-%d')

print(dt.strftime('%Y-%m-%d'))
print(yesterday.strftime('%Y-%m-%d'))
print(last_month())

dt_string = '01/01/17 12:10:03.234567'
dtnew = datetime.strptime(dt_string, '%d/%m/%y %H:%M:%S.%f')