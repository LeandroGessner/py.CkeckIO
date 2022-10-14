from typing import Iterable

def replace_last(line: list) -> Iterable:
    if len(line) == 0 or len(line) == 1:
        return line
    else:
        last = line.pop()

        return [last] + line


if __name__ == "__main__":
    print('Example:')
    print(list(replace_last([2, 3, 4, 1])))

    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []

    print("The mission is done! Click 'Check Solution' to earn rewards!")