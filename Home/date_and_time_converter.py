from datetime import datetime

def date_time(time: str) -> str:
    date = datetime.strptime(time, "%d.%m.%Y %H:%M")

    hours = "hour" if int((((time.split(" "))[1]).split(":"))[0]) == 1 else "hours"
    minutes = "minute" if int((((time.split(" "))[1]).split(":"))[1]) == 1 else "minutes"

    format = "%#d %B %Y year %#H " + hours  + " %#M " + minutes
    
    # For windows -> "#"
    # For unix -> "-"
    return date.strftime(format)


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 01:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")