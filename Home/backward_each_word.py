def backward_string_by_word(text: str) -> str:
    inverted_text = ' '.join(word[::-1] for word in text.split(' '))

    return inverted_text


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    backward_string_by_word('')
    backward_string_by_word('world')
    backward_string_by_word('hello world')
    backward_string_by_word('hello   world')
    backward_string_by_word('welcome to a game')
    print("Coding complete? Click 'Check' to earn cool rewards!")
