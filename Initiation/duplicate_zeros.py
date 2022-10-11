def duplicate_zeros(donuts: list) -> list:
    final_list = []

    for index, number in enumerate(donuts):
        if number == 0:
            zeros = [0, 0]
            final_list.extend(zeros)
        else:
            final_list.append(number)

    return final_list


print("Example:")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")