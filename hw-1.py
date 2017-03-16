date1 = input ('Введите первую дату: ')
date2 = input ('Введите вторую дату: ')
if date1 == date2:
	print('1')
elif (len(date1)>len(date2)) & (date2 != 'learn'):
	print('2')
elif len(date1) != len(date2):
	if date2 == 'learn':
		print('3')
	else:
		print('No')