def translate(text: str) -> str:
    vowels = 'aeiouy'

    text = list(text)

    clean_text = []

    for index, letter in enumerate(text):
        if letter not in vowels:
            clean_text.append(letter)
        elif letter in vowels and text[index - 1] not in vowels:
            pass
        else:
            clean_text.append(letter)

    return clean_text


if __name__ == "__main__":
    # print("Example:")
    # print(translate("hieeelalaooo"))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert translate("hieeelalaooo") == "hello"
    # assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    # assert translate("aaa bo cy da eee fe") == "a b c d e f"
    # assert translate("sooooso aaaaaaaaa") == "sos aaa"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print(translate("sooooso aaaaaaaaa"))