def negabinary_to_decimal(negabinary_list):
    decimal_number = 0
    negabinary_list.reverse()

    for i, bit in enumerate(negabinary_list):
        decimal_number += bit * ((-2) ** i)

    return decimal_number

def decimal_to_negabinary(decimal_number):
    negabinary_list = []

    while decimal_number != 0:
        remainder = decimal_number % (-2)
        decimal_number //= (-2)

        # Adjust for negative remainders
        if remainder < 0:
            remainder += 2
            decimal_number += 1

        negabinary_list.append(remainder)

    return negabinary_list[::-1]



arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]

d1 = negabinary_to_decimal(arr1)
d2 = negabinary_to_decimal(arr2)
d = d1 + d2
arr = decimal_to_negabinary(d)

print(arr, ' = ', d)

arr1 = [0]
arr2 = [1]

d1 = negabinary_to_decimal(arr1)
d2 = negabinary_to_decimal(arr2)
d = d1 + d2
arr = decimal_to_negabinary(d)

print(arr, ' = ', d)