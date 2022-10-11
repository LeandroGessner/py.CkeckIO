from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    dawn = float(6 * 60)
    nightfall = float(18 * 60)

    hours = float((time.split(":"))[0])
    minutes = float((time.split(":"))[1])

    total_minutes = hours * 60 + minutes

    return (dawn)


if __name__ == '__main__':
    # print("Example:")
    # print(sun_angle("07:00"))

    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert sun_angle("07:00") == 15
    # assert sun_angle("01:23") == "I don't see the sun!"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print(sun_angle('07:00'))