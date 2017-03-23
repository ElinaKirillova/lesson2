def find_person(name):
	list_names = ["Вася", "Маша", "Петя",
	              "Валера", "Саша", "Даша"]
	current_name = list_names.pop(0)
	while current_name != name:
		current_name = list_names.pop(0)
		if len(list_names) == 0:
			return "Имени {0} нет :С".format(name)
	else:
		return '{0} нашелся!'.format(name)

answer = find_person('Валера')
answer1 = find_person('Маша')
answer2 = find_person('Гаша')
print(answer, answer1, answer2)