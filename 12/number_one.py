lista = [2,7,5,3,6]
cel = 9

def funk(l, c):
    length = len(l)
    result = []
    for i in range(0, length):
        for j in range(i+1, length):
            if c == l[j] + l[i]:
                result.append((i, j))
    return result

print(funk(lista, cel))