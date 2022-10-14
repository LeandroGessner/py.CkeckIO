from typing import Union


def sun_angle(time: str) -> Union[int, str, float]:
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = round(int(minutes) / 60, 2)

    hour = hours + minutes

    if 6 <= hour <= 18:
        return (hour - 6) * 15
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
