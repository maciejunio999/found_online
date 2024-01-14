from itertools import combinations


def find_combinations(numbers, target):
    result = []

    for r in range(1, len(numbers) + 1):
        index_combinations = combinations(range(len(numbers)), r)

        for indices in index_combinations:
            if sum(numbers[i] for i in indices) == target:
                result.append(tuple(indices))

    return result



numbers_list = [1, 2, 3, 4, 5]
target_sum = 7

combinations_result = find_combinations(numbers_list, target_sum)
print("Combinations:", combinations_result)
