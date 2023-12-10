import random

def funk(n, r):
    numbers = [i for i in range(10, 100, 1)]
    result = []
    for i in numbers:
        if r == i % n:
            result.append(i)
    return result



helping = [(random.randint(0 ,100), random.randint(0, 100)) for i in range(0,11)]
tests = []
for i in helping:
    if i[1] < i[0]:
        tests.append(i)


for i in tests:
    print('Dzielna i reszta: ', i, '\n', 'Rezultaty: ',funk(i[0], i[1]), '\n')