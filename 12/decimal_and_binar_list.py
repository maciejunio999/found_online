def binary_to_decimal(binary_list):
    decimal_number = 0
    binary_list.reverse()

    for i, bit in enumerate(binary_list):
        decimal_number += bit * (2 ** i)

    return decimal_number

def decimal_to_binary(decimal_number, list_length):
    binary_list = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_list.append(remainder)
        decimal_number //= 2

    binary_list = [0] * (list_length - len(binary_list)) + binary_list

    return binary_list


binary_representation = [1, 0, 1, 1]
decimal_result = binary_to_decimal(binary_representation)
print(f"Decimal representation: {decimal_result}")


decimal_input = 11
binary_result = decimal_to_binary(decimal_input, list_length=5)
print(f"Binary representation: {binary_result}")
