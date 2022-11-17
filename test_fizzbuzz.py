def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    return str(number)


def test_fizz_1_is_1():
    assert fizzbuzz(1) == "1"


def test_fizz_2_is_2():
    assert fizzbuzz(2) == '2'


def test_fizzbuzz_3_is_fizz():
    assert fizzbuzz(3) == 'fizz'


def test_fizzbuzz_5_is_buzz():
    assert fizzbuzz(5) == 'buzz'


def test_fizzbuzz_15_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'
