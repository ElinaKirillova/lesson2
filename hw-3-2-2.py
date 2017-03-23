list_names = ["Вася", "Маша", "Петя",
              "Валера", "Саша", "Даша"]

def find_person(name):
	if name in list_names:
		return '{0} нашелся!'.format(name)
	return "Имени {0} нет :С".format(name)

answer = find_person('Валера')
answer1 = find_person('Маша')
answer2 = find_person('Гаша')
print(answer, answer1, answer2)