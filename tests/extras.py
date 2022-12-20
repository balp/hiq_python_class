value = 2


def names():
    return ['A', 'B']


def some_starange_name():
    return ['A', 'B', 'C']


def increase(number) -> None:
    global value
    value += number

def get():
    return value
