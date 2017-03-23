def wordcounted(phrase):
	return len(phrase.split(' '))

if __name__ == '__main__':
	phrase = input('Введите вашу фразу: ')
	count = wordcounted(phrase)
	print('{0} слова'.format(count))