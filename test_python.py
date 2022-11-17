
def test_integers():
    assert 1 + 2 == 3


def test_variables():
    age = 50
    age = age + 1
    assert age == 51


def test_strings():
    name = "Anders"
    also_name = str('Anders')
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

    assert 0xf & 0x3 == 0x3
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
    x /= 2
    z = 9
    z %= 2
    z //= 3
    z **= 2

    b = 0xf
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
    assert ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][-4:-1] == ["orange", "kiwi", "melon"]
