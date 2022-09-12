def from_camel_case(name: str) -> str:
    word_with_separator = ''

    for letter in name:
        if letter.isupper():
            word_with_separator = word_with_separator + '_' + letter
        else:
            word_with_separator = word_with_separator + letter

    return word_with_separator.lower()[1:]

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")