def is_perfect(n: int) -> bool:
    divisors = [number for number in range(1, n) if n % number == 0]

    return False if sum(divisors) != n else True


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True  # noqa: E712
assert is_perfect(2) == False  # noqa: E712
assert is_perfect(28) == True  # noqa: E712
assert is_perfect(20) == False  # noqa: E712
assert is_perfect(496) == True  # noqa: E712
assert is_perfect(30) == False  # noqa: E712
assert is_perfect(8128) == True  # noqa: E712
assert is_perfect(100) == False  # noqa: E712
assert is_perfect(500) == False  # noqa: E712
assert is_perfect(1000) == False  # noqa: E712

print("The mission is done! Click 'Check Solution' to earn rewards!")
