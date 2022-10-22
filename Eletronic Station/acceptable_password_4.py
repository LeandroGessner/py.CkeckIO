import re


def is_acceptable_password(password: str) -> bool:
    size = len(password)
    has_digit = bool(re.search(r'\d', password))

    if (6 < size <= 9 and not password.isdigit()) and has_digit:
        return True
    elif (size > 9 and password.isdigit()):
        return True
    else:
        return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    # assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    # assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")