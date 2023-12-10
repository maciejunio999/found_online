from collections import Counter


def count_occurrences(input_list):
    return dict(Counter(input_list))


def find_max_occurrence(dictionary):
    if not dictionary:
        return None, None  # Return None if the dictionary is empty
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value


def indeksy(input_list, element):
    result = []
    for i in range(0, len(input_list)):
        if element == input_list[i]:
            result.append(i)
    return result


def drop_most_common(input_list, element, indexes):
    result = input_list[:]
    for i in indexes:
        result[i] = '_'
    try:
        while result.index('_') >= 0:
            result.remove('_')
    except ValueError:
        return result


def copy_first_and_add_to_list(input_list):
    x = input_list[0]
    return [x] + input_list[:] + [x]


def remove_duplicates_and_sort(input_list):
    unique_elements = list(set(input_list))  # Remove duplicates
    sorted_list = sorted(unique_elements)    # Sort the unique elements
    return sorted_list


def odd_and_even(input_list):
    odd, even = [], []
    for i in range(0, len(input_list)):
        if 0 == i % 2:
            even.append(input_list[i])
        elif 1 == i % 2:
            odd.append(input_list[i])
    return odd + even


def funk(l):
    print("Długość: ", len(l), '\n')
    my_dict = count_occurrences(l)
    max_common, how_common = find_max_occurrence(my_dict)
    print(f"Najczęściej występujący element: {max_common} (wystąpienia: {how_common})", '\n')
    indexes = indeksy(l, max_common)
    print("Indeksy: ", indexes, '\n')
    l = drop_most_common(l, max_common, indexes)
    print("Po usunięciu najczęściej występującego elementu: ", l, '\n')
    l = copy_first_and_add_to_list(l)
    print("Po dodaniu elementu z pozycji [0] na początku i końcu listy: ", l, '\n')
    l = remove_duplicates_and_sort(l)
    print("Po usunięciu powtórzeń i sortowaniu: ", l, '\n')
    l = odd_and_even(l)
    print("Nowa kolejność: ", l, '\n')


lista = [7, 2, 4, 5, 2, 3, 7, 6, 5, 0, 2, 1, 0, 2]
funk(lista)

print('#' * 100)

lista = ['jeden', 'dwa', 'dwa', 'jeden', 'trzy', 'jeden', 'cztery', 'zero']
funk(lista)