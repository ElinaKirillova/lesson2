def wordcounted(phrase):
	return len(phrase.split(' '))
phrase = input('Введите вашу фразу: ')
count = wordcounted(phrase)
print('{0} слова'.format(count))