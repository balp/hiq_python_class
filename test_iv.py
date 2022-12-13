def add_one(x):
    return x + 1


def test_lamba():
    list = [1, 2, 3, 4]
    number = 1
    map(lambda val: val + number, list)
    map(add_one, list)


def test_list():
    fruits = ["Apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    afruit = any([x.istitle() for x in fruits if 'e' in x])

    print(afruit)


class NameOfClass:
    value = 1

    def __init__(self, value) -> None:
        self.data = 1
        self._v = value

    def func(self):
        self.value = 2

    def func2(self):
        return self.value + self._v


def test_class():
    a = NameOfClass(45)
    assert a.data == 1
    a.func()
    assert a.value == 2


class Animal:
    def __init__(self):
        self._spices = None

    def species(self):
        return self._spices

    def legs(self):
        return 2


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self._spices = "Dog"

    def legs(self):
        return 4


def test_dog():
    dog = Dog()
    assert dog.species() == "Dog".capitalize()
    assert dog.legs() == 4
