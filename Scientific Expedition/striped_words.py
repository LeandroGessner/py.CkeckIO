import re


VOWELS = 'AEIOUY'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXZ'


def unlegal_letter_sequence(word: str) -> bool:
    if len(word) <= 1:
        return False
    
    if word.isdigit():
        return False
    
    if not word.isalpha():
        return False

    for i in range(0, len(word) - 1):
        if (word[i] in VOWELS and word[i + 1] in VOWELS) or (word[i] in CONSONANTS and word[i + 1] in CONSONANTS):
            return False
    
    return True
        

def checkio(line: str) -> int:
    line = line.upper()

    words = [item for item in re.split(r"[,. ?!;]", line) if item != '']

    final_list = [word for word in words if unlegal_letter_sequence(word)]
            
    return len(final_list)


if __name__ == "__main__":
    print("Example:")
    print(checkio("My name is ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("My name is ...") == 3
    assert checkio("Hello world") == 0
    assert checkio("A quantity of striped words.") == 1
    assert checkio("Dog,cat,mouse,bird.Human.") == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
