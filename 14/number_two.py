def dzielenie_z_resztą(x):
    pelne = x // 10
    reszta = x % 10
    return pelne, reszta

def funk(x, y, bound):
    m = 0 # wyniki spełniające warunek
    n = 0 # liczba pomagająca określić wartości w potęgach
    result = [] # lista poprawnych wyników
    pomocniczy = 0 # liczy ilość przypadków w ktorych parametry nie spełniają warunków, potrzebne żeby
                   # program nie wykonywał zbyt wiele operacji

    while True:
        if pomocniczy < 50:
            i, j = dzielenie_z_resztą(n)
            print(i, j)
            m = x ** i + y ** j
            n += 1
        else:
            break

        if m <= bound and m not in result:
            result.append(m)
        else:
            pomocniczy += 1

    result.sort()

    return result

print(funk(2, 3, 10))