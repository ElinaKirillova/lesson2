list_answers = ['хорошо', 'булка', 'Патрик', 'Хорошо']

def ask_user():
	answer_user = None
	while not (answer_user in list_answers):
		answer_user = input('Как дела? Ваш ответ: ')

ask_user()