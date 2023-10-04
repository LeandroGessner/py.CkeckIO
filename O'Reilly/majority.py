def is_majority(items: list[bool]) -> bool:
    if len(items) == 0:
        return False
    else:
        trues = 0
        falses = 0

        for boolean in items:
            if boolean:
                trues += 1
            else:
                falses += 1
        
        if trues > falses:
            return True
        else:
            return False

    return True


print("Example:")
print(is_majority([True, True, False, True, False]))

assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
