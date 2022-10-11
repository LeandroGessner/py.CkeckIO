def missing_number(items: list[int]) -> int:
    items = sorted(items)

    min_num = min(items)
    max_num = max(items)
    step = min((items[1] - items[0]), (items[-1] - items[-2]))
    
    lst = [item for item in range(min_num, max_num, step)]

    for item in lst:
        if item not in items:
            return item


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")