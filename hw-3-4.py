list_answers = ['Пока', 'пока', 'Пока!', 'пока!']

def get_answer():
	answer_user = None
	while not answer_user in list_answers:
		answer_user = input('Спроси что-нибудь: ')
		if answer_user not in list_answers:
			print('Согласен с тобой!')

get_answer()
