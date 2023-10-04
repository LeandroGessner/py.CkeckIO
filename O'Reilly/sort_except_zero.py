from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    # getting the indexes of all zeros in the original list
    zeros_index = [index for index, value in enumerate(items) if value == 0]

    # excluding the zeros and sorting the items in the original list
    items_without_zeros = sorted([value for value in items if value != 0])

    # reinserting the zeros in the right place
    for index in zeros_index:
        items_without_zeros.insert(index, 0)

    return items_without_zeros


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
