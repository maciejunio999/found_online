def numMovesStones(stones):
    stones.sort()
    n = len(stones)

    # Calculate the maximum moves
    max_moves = max(stones[n - 1] - n + 2 - stones[1], stones[n - 2] - stones[0] - n + 2)

    # This loop calculates the minimum moves by checking the gap between consecutive stones.
    # If there is a gap larger than 1, it implies that there is a free space between two stones,
    # and it requires at least n - (gap) + 1 moves to fill that gap.
    min_moves = n
    for i in range(n - 1):
        if stones[i + 1] - stones[i] == 1:
            continue
        min_moves = min(min_moves, n - (stones[i + 1] - stones[i]) + 1)

    # If the first two stones or the last two stones have a gap larger than 1, it implies that there is
    # room to move one of the endpoint stones to fill the gap. In this case, it takes at most 2 moves.
    if stones[1] - stones[0] > 1:
        min_moves = min(min_moves, 2)
    if stones[n - 1] - stones[n - 2] > 1:
        min_moves = min(min_moves, 2)

    return [min_moves, max_moves]

# Example 1
stones1 = [7, 4, 9]
output1 = numMovesStones(stones1)
print(output1)  # Output: [1, 2]

# Example 2
stones2 = [6, 5, 4, 3, 10]
output2 = numMovesStones(stones2)
print(output2)  # Output: [2, 3]