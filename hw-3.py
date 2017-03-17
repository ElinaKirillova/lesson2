list_names = ["Вася", "Маша", "Петя",
              "Валера", "Саша", "Даша"]

current_name = list_names.pop(0) 

while current_name != 'Валера':
	current_name = list_names.pop(0)
	if len(list_names) == 0:
		break
else:
	print('Валера нашелся!')