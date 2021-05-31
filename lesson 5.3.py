tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) < len(klasses):
    max_n_ = len(klasses)
    num = len(klasses) - len(tutors)
    for i in range(num):
        tutors.append(None)
elif len(tutors) > len(klasses):
    max_n_ = len(tutors)
    num = len(tutors) - len(klasses)
    for k in range(num):
        klasses.append(None)

a = ((tutors[i], klasses[i]) for i in range(max_n_))

print(type(a))
for ii in range(max_n_):
    print(next(a))