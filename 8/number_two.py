import numpy as np

num_of_coefficients = 5

coefficients = list(np.linspace(1, 12, num=num_of_coefficients))
coefficients.reverse()

borders = [0,5]

num_of_points = 3


def calculate(coeff, bor, number_of_points):
    results = []
    random_list_of_points = list(np.linspace(bor[0], bor[1], num=number_of_points))
    print(random_list_of_points)
    for x in random_list_of_points:
        result = 0
        for i in range(0, len(coeff)):
            #print(coeff[i], x)
            result += coeff[i] * (x**i)
        results.append(result)
    return results

calculate(coefficients, borders, num_of_points)