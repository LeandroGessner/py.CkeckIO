import re

def words_order(text: str, words: list) -> bool:
    indexes_list = []

    for word in words:
        if words.count(word) > 1:
            return False
        elif not re.search(f'\\b{word}\\b', text):
            return False
        else:
            indexes_list.append(text.index(word))
    
    for index in range(len(indexes_list) - 1):
        if indexes_list[index] > indexes_list[index + 1]:
            return False

    return True


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")