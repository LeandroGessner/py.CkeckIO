def changing_direction(elements: list[int]) -> int:
    direction = ''
    counter = 0

    for id, val in enumerate(elements):
        if id < len(elements) - 1:
            if val > elements[id + 1] and direction == 'up':
                counter += 1
            elif val < elements[id + 1] and direction == 'down':
                counter += 1
            
            if val > elements[id + 1]:
                direction = 'down'
            elif val < elements[id + 1]:
                direction = 'up'
            

    return counter


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
