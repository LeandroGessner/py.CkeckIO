def int_palindrome(number: int, B: int) -> bool:
    res = number // B
    bin = []

    if res > 1:
        int_palindrome(res, B)
    else:
        bin.append(str(res))
    
    return bin


# print("Example:")
# print(int_palindrome(455, 2))

# assert int_palindrome(6, 2) == False
# assert int_palindrome(34, 2) == False
# assert int_palindrome(455, 2) == True

# print("The mission is done! Click 'Check Solution' to earn rewards!")

print(int_palindrome(6, 2))
