from datetime import date, timedelta

def days_diff(a, b):
    c = date(a[0], a[1], a[2])
    d = date(b[0], b[1], b[2])

    return (abs(d - c).days)


if __name__ == "__main__":
    print("Example:")

    days_diff((1982, 4, 19), (1982, 4, 22))
    days_diff((2014, 1, 1), (2014, 8, 27))
    days_diff((2014, 8, 27), (2014, 1, 1))
    days_diff((2014, 2, 28), (2014, 2, 28))
