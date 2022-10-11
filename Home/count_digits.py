def count_digits(text: str) -> int:
    counter = 0

    for letter in text:
        if letter.isdigit():
            counter += 1
    
    return counter


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    count_digits('hi')
    count_digits('who is 1st here')
    count_digits('my numbers is 2')
    count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')
    count_digits('5 plus 6 is')
    count_digits('')
    print("Coding complete? Click 'Check' to earn cool rewards!")
