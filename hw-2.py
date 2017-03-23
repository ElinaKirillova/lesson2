journals =[
    {'school_class': '1a', 'scores': [5, 4, 3, 2, 5, 4, 4, 4, 5, 5, 3, 5]}, 
    {'school_class': '1b', 'scores': [5, 5, 4, 3, 2, 5, 4, 5, 4, 3]},
    {'school_class': '2a', 'scores': [5, 4, 3, 4, 3, 3, 3, 4, 5, 4, 5]}
]

def calc_mean(array):
    return sum(array) / len(array)

all_classes_means = 0
all_classes_count = len(journals)

for journal in journals:
    scores = journal['scores']
    school_class = journal['school_class']
    mean = calc_mean(scores)
    all_classes_means += mean
    print('%s -- %0.1f' % (school_class, mean))
    
school_mean = all_classes_means / all_classes_count
print ('Средний балл по школе — %0.1f' % school_mean)