def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """

    count_1: int = 1
    count_2: int = 0

    for index, item in enumerate(line):
        if index < len(line) - 1:
            if item == line[index + 1]:
                count_1 += 1
            else:
                count_1 = 1
            
        if count_1 > count_2:
            count_2 = count_1

    return count_2


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")