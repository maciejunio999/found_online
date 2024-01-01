x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0] 
y = [0.0, 1.125, 2.5, 4.125, 6.0, 8.125, 10.5]

def derivative(xs, ys):
    lista = []
    for i in range(1, len(xs)):
        dy = (ys[i] - ys[i - 1])/(xs[i] - xs[i - 1])
        lista.append(dy)
    return lista

print(derivative(x, y))