import time


def get_date() -> str:
    gotten_date = time.strftime("%d %b %Y")
    return gotten_date

def get_time() -> str:
    gotten_time = time.strftime("%H : %M")
    return gotten_time