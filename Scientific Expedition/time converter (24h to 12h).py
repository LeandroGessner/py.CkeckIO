from datetime import datetime


def time_converter(time):
    am_pm = '.'.join(datetime.strftime(datetime.strptime(time, '%H:%M'), '%p').lower()) + '.'
    return datetime.strftime(datetime.strptime(time, '%H:%M'), '%#I:%M ' + am_pm)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")