import csv
with open ('answers.csv', 'w', encoding='utf-8') as f:
    answers = {'hello':'угу',
               'hru':'ОК НОРМ',
               'бай':'бай'
               }
    fields = ['ключ', 'значение']
    writer = csv.DictWriter(f, fields, delimiter = ';')
    writer.writeheader()
    f.write(writer)