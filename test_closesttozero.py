# closest to zero
# en funktion som tar in en lista av heltal
# och returnerar det värde som är närmat noll
# om två värden är lika nära skall det possitiva returneran
from typing import Dict, List, Any


#   closest([1, 2, 3, 4]) -> 1
#   closest([-2, -4, -6]) -> -2
#   closest([2, -2]) -> 2


def closest_to_zero(numbers: List[int]) -> int:
    closest = numbers[0]
    for number in numbers:
        if abs(number) == abs(closest):
            closest = max(number, closest)
        if abs(number) < abs(closest):
            closest = number
    return closest


def test_list_with_one_element() -> None:
    assert closest_to_zero([1]) == 1


def test_list_with_one_other_element() -> None:
    assert closest_to_zero([2]) == 2


def test_secone_elementy_is_closest() -> None:
    assert closest_to_zero([2, 1]) == 1


def test_negative_numbers() -> None:
    assert closest_to_zero([-2, -1]) == -1


def test_return_possitive_on_equal() -> None:
    assert closest_to_zero([-2, 2]) == 2


def test_return_possitive_on_equal_2() -> None:
    assert closest_to_zero([2, -2]) == 2
