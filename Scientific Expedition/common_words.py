import re


def checkio(line1: str, line2: str) -> str:
    final_string = [word for word in line1.split(',') if re.search(f'\\b{word}\\b', line2)]

    return ','.join(sorted(final_string))


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
