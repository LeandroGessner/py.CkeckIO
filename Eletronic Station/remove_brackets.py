import re


def remove_brackets(line: str) -> str:
    return re.findall(r"\(.*\)", line)


if __name__ == "__main__":
    # print("Example:")
    # print(remove_brackets("(()()"))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert remove_brackets("(()()") == "()()"
    # assert remove_brackets("[][[[") == "[]"
    # assert remove_brackets("[[(}]]") == "[[]]"
    # assert remove_brackets("[[{}()]]") == "[[{}()]]"
    # assert remove_brackets("[[[[[[") == ""
    # assert remove_brackets("[[[[}") == ""
    # assert remove_brackets("") == ""
    # assert remove_brackets("[(])") == "()"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print(remove_brackets("(()()"))