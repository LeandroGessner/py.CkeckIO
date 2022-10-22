def clean_dict(dictionary: dict) -> dict:
    keys_with_zero_values = [key for key, value in dictionary.items() if dictionary[key] == 0 or key == '']

    for item in keys_with_zero_values:
        dictionary.pop(item)

    return dictionary


def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    my_dict = {}

    for tup in data:
        key, value = tup[0], tup[1]

        if key in my_dict:
            my_dict[key] += value
        else:
            my_dict[key] = value

    return clean_dict(my_dict)


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
