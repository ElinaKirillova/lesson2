def wordcount(phrase):
	return len(phrase.split(' '))
phrase = input('Введите вашу фразу: ')
count = wordcount(phrase)
print('{0} слова'.format(count))