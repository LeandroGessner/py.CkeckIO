def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    lst = set(data)

    my_dict = {f'{item}':data.count(item) for item in lst}

    return max(my_dict, key=my_dict.get)


if __name__ == "__main__":
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")