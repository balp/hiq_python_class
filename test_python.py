def test_integers():
    assert 1 + 2 == 3


def test_variables():
    age = 50
    age = age + 1
    assert age == 51


def test_strings():
    name = 'Anders'
    also_name = str("Anders")
    assert name == also_name


def test_integers2():
    a = 1
    b = 12345678901234567890
    assert a < b


def test_floats():
    a = 1.0
    b = 2.0
    c = 1.0
    d = 1e10
    f = 1.2e10
    e = float("2.3")
    print(a, b, c, d, e)
    assert a < b
    assert c < b
    assert a == c


def test_bool():
    a = True
    b = False
    assert a != b


def test_operators():
    assert 1 + 2 == 3
    assert 2 - 1 == 1
    assert 3 * 3 == 9
    assert 9 / 3 == 3
    assert 9 / 2 == 4.5
    assert 9 % 2 == 1
    assert 9 // 2 == 4
    assert 2 ** 3 == 8

    assert 0xF & 0x3 == 0x3
    assert 0x4 | 0x3 == 0x7
    assert 0x4 ^ 0x3 == 0x7
    assert ~0x3 == -4
    assert 0x1 << 1 == 0x2
    assert 0x2 >> 1 == 0x1


def test_assignment_operatots():
    x = 5
    x += 1
    x -= 2
    x *= 2
    x /= 2
    z = 9
    z %= 2
    z //= 3
    z **= 2

    b = 0xF
    b &= 0x3
    b |= 0x1
    b ^= 0x6
    b >>= 1
    b <<= 1


def test_lists():
    assert "one" in ["one", "two"]
    assert 2 == len(["one", "two"])
    assert 3 == len(list(("apple", "banana", "cherry")))
    assert "one" == ["one", "two"][0]
    assert "two" == ["one", "two"][-1]
    assert ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][-4:-1] == [
        "orange",
        "kiwi",
        "melon",
    ]
    for n in ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]:
        assert len(n) > 0


def test_tuple():
    assert "one" in ("one", "two")
    assert 1 == len(("one",))
    assert True in (1, 5, 3.4, "One", True)
    assert "one" == ("one", "two")[0]
    assert "two" == ("one", "two")[-1]


def test_set():
    assert "apple" in {"banana", "pear", "apple"}
    assert 3 == len({"banana", "pear", "apple"})
    assert 3 == len({"banana", "pear", "apple", "pear"})


def test_dictionaries():
    assert "hi" in {"hi": "Hej", "Bye": "Hej då"}
    assert 1234 == {"hi": "Hej", "Bye": "Hej då", "år": 1234, 12: 12}["år"]
    d = {}
    d[10] = 11
    assert d[10] == 11
    car = {"model": "EX90"}
    # Loop
    for key in car.keys():
        assert key == "model"
    for value in car.values():
        assert value == "EX90"
    for key, value in car.items():
        assert key == "model"
        assert value == "EX90"
    # Remove
    values = {"a": 10, "b": 20, "c": 30}
    values.pop("b")
    assert "b" not in values
    del values["c"]
    assert "c" not in values

    reference = values
    copy = values.copy()
    values["d"] = 40
    assert "d" in reference
    assert "d" not in copy


def test_while():
    number = 1
    while number < 10:
        print(number)
        assert number * 5 < 40
        if number % 3 == 0:
            break
        if number % 2 == 0:
            number += 2
            continue
        number += 1
    else:
        assert number > 4


def test_for():
    for fruit in ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]:
        print(fruit)
        if fruit == "banana":
            continue
        if fruit == "cherry":
            break
    for n in range(10):
        print(n)


def my_helper():
    """Function without arguments"""
    pass


def get_well_greeting(wishes, to):
    """Key word arguments"""
    return f"Get well {to}, wishes {wishes}."


def greetings_class(*names):
    """Any number of arguments"""
    return f"Hej, {', '.join(names)}!"


def test_functions():
    assert my_helper() is None
    assert get_well_greeting("Anders", "Sara") == "Get well Sara, wishes Anders."
    assert (
            greetings_class("Strategin", "Petra", "Victor", "Jenny", "Peter")
            == "Hej, Strategin, Petra, Victor, Jenny, Peter!"
    )
    assert get_well_greeting(wishes="Anders", to="Sara") == "Get well Sara, wishes Anders."


def test_lambda():
    func = lambda x: x * x
    assert func(2) == 4
    lista = [1, 2, 3, 4]
    assert list(map(lambda x: x + 1, lista)) == [2, 3, 4, 5]


def test_list_comprehension():
    fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    afruit = [x for x in fruits if 'a' in x]
    assert afruit == ['apple', 'banana', 'orange', 'mango']
    assert [x for x in range(3)] == [0, 1, 2]
    assert [x.capitalize() for x in afruit] == ['Apple', 'Banana', 'Orange', 'Mango']
    assert [f if f != 'banana' else 'orange' for f in afruit] == ['apple', 'orange', 'orange', 'mango']


def test_simple_class() -> None:
    class Student:
        def __init__(self, name: str):
            self.name = name

    petra = Student('Petra')
    assert petra.name == 'Petra'

    class Person:
        def __init__(self, first_name, last_name) -> None:
            self.first_name = first_name
            self.last_name = last_name

        def full_name(self) -> str:
            return f"{self.first_name} {self.last_name}"

    anders = Person(last_name="Arnholm", first_name="Anders")
    assert anders.full_name() == "Anders Arnholm"
