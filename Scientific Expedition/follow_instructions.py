def follow(instructions: str) -> tuple[int, int] | list[int]:
    my_list = [0, 0]

    for letter in instructions:
        if letter == 'f':
            my_list[1] += 1
        elif letter == 'b':
            my_list[1] -= 1
        elif letter == 'l':
            my_list[0] -= 1
        elif letter == 'r':
            my_list[0] += 1

    return my_list


print("Example:")
print(list(follow("fflff")))

assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
