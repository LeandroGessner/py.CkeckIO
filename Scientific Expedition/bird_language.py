def translate(text: str) -> str:
    letters = "aeiouy"
    new = ''
    index = 0

    while index < len(text):
        if text[index] == ' ':
            new += text[index]
        elif text[index] not in letters and text[index + 1] in letters:
            new += text[index]
            index += 1
        elif text[index] in letters:
            if text[index:index + 3] == text[index] * 3:
                new += text[index]
                index += 2
        index += 1
    
    return new


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
