import enum


def changing_direction(elements: list) -> int:
    counter = 0
    
    for index, number in enumerate(elements):
        if ((index > 0) and (elements[index - 1] > elements[index])) and (index < len(elements) and (elements[index + 1] < elements[index])):
            counter += 1
        
        print(number)

    return counter


# print("Example:")
# print(changing_direction([1, 2, 3, 4, 5]))

# assert changing_direction([1, 2, 3, 4, 5]) == 0
# assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

changing_direction([1, 2, 3, 2, 1])