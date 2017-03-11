def get_answer(question):
	answers = {'hello':'угу', 'hru':'ОК НОРМ', 'бай':'бай'}
	return answers[question.lower()].lower()
question = input('Ваш вопрос?')
print (str(get_answer(question)))
