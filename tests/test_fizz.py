# fizz(1) -> "1"
# fizz(2) -> "2"
# fizz(3) -> "Fizz"
# fizz(4) -> "4"
# fizz(5) -> "Buzz"
# fizz(6) -> "Fizz"
# ....
# fizz(15) -> "FizzBuzz"


def fizz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


def test_1_1() -> None:
    assert fizz(1) == "1"


def test_2_2() -> None:
    assert fizz(2) == "2"


def test_3_Fizz() -> None:
    assert fizz(3) == "Fizz"


def test_6_Fizz() -> None:
    assert fizz(6) == "Fizz"


def test_5_Buzz() -> None:
    assert fizz(5) == "Buzz"


def test_10_Buzz() -> None:
    assert fizz(10) == "Buzz"


def test_15_FizzBuzz() -> None:
    assert fizz(15) == "FizzBuzz"


def test_30_FizzBuzz() -> None:
    assert fizz(30) == "FizzBuzz"
