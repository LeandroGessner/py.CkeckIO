from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    els = list(els)

    if len(els) < 3:
        return els
    else:
        a = list(els)[0:2]

        for id, item in enumerate(els):
            if id < len(list(els)) - 2:
                a.append(sorted(els[id:id + 3])[1])

    return a


print('Example:')
print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

assert median_three([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert median_three([1]) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
