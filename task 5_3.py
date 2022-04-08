from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А',]

my_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))
print(type(my_gen))
for i in tutors:
    print(next(my_gen))
