def caps_lock(text: str) -> str:
    caps = 0
    phrase = ''

    for letter in text:
        if letter == 'a' and caps == 0:
            caps = 1
        elif letter == 'a' and caps == 1:
            caps = 0

        if letter == 'a' or letter == 'A':
            continue
        else:
            if caps == 1:
                phrase += letter.upper()
            else:
                phrase += letter.lower()

    return phrase


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
