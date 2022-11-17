def add(a, b):
    return a + b


def test_false():
    assert True


def test_1_1_2():
    assert add(1, 1) == 2


def test_variabel():
    x = 1
    y = 2894273483248723678423864872364873264872364876237846238746287346872364872364782364782
    z = x + y
    assert z == 3

def test_strings():
    """Test some strings

    ...
    """
    a = "And''ers"
    b = 'and""ers'
    assert a == b.capitalize()

def test_float():
    a = 2
    b = 5.6
    c = 12e4
    assert a - b + c == 5

def test_bool():
    a = True
    b = False
    assert a != b

def test_operators():
    assert 1 + 2 == 3
    assert 1 - 2 == -1
    assert 1 * 2 == 2
    assert 1 / 2 == 0.5
    assert 1 % 2 == 0
    assert 1 // 2 == 0
    assert 2 ** 2 == 4


def test_assign():
    a = 1
    a += 1
    assert a == 2
