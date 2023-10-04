def final_stone(stones: list[int]) -> int:
    stones = sorted(stones, reverse=True)

    new_stones = []

    new_stones.append(stones[0] - stones[1])
    new_stones.extend(stones[2:])
    
    if new_stones[0] < new_stones[1] \
            or new_stones[1] == new_stones:
        return 0
    else:
        return new_stones[0] - new_stones[1]

print('Example:')
print(final_stone([1,2,3]))

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
# assert final_stone([1, 1, 1, 1]) == 0
# assert final_stone([1, 1, 1]) == 1
# assert final_stone([1, 10, 1]) == 8
# assert final_stone([1, 10, 1, 8]) == 0
# assert final_stone([]) == 0
# assert final_stone([1]) == 1
# assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")

# print(final_stone([3, 5, 1, 1, 9]))
