import math

def convert(seconds):
    if seconds < 60:
        return (0, 0, seconds)
    elif 60 <= seconds < 3600:
        second = seconds % 60
        minute = math.floor(seconds/60)
        return (0, minute, second)
    else:
        second = seconds % 60
        hour = math.floor(seconds/(60*60))
        minute = math.floor(seconds/60) - 60*hour
    return (hour, minute, second)

