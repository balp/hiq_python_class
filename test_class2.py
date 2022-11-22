def test_list():
    l = ["one",
         1,
         True,
         [],
         [1, 2],
         [],
         ]
    assert len(l) == 6
    tva = list((1, 2))
    assert l[0] == "one"
    l[0] = "two"
    assert l[-1] == []
    assert l[:2] == ["one", 1, ]
    assert l[:-3] == ["one", 1, True]
    assert l[:3] == []
    l += [1, 2]
    l.append(2)
    l.pop()


def test_tuple():
    a = (1, 2)
    b = (1,)
    assert a[0] == 1
    assert len(b) == 1


def test_set():
    assert len({1, 2, 3}) == 3
    assert len({1, 2, 3, 1}) == 3


def test_dict():
    a = {1: 2, 2: 4}
    b = a[1]
    a = {"name": "Anders", "class": "python"}
    b = a["name"]
    a["name"] = "Balp"
    if "name" in a:
        pass
    a.pop("name")
    del a["class"]
    if "class" not in a:
        pass

    c = {"a": 4, "H": 5}
    d = c
    e = c.copy()
    f = dict(c)
    c["a"] = 6
    assert d["a"] == 6
    assert e["a"] == 4
    assert f["a"] == 4


def test_while():
    a = 0
    while a < -10:
        a = a + 1
        if a > 5:
            break
        if a == 2:
            continue
        print(a)
    else:
        print(a)


def test_for():
    a = [1, 2, 3]
    a = (1, 2, 3)
    a = {"a": 1, "b": 2}
    b, c = (1, 2)
    for key, value in a.items():
        print(key, value)
    for n in range(10):
        print(n)


def greet(name: str) -> str:
    """Greets a person
    """
    return f"Hi {name.capitalize()}"


def hello(a, b):
    greet(name=str(a))


def long(*args):
    print(len(args))


def kw(**kwargs):
    print(kwargs)


def too_complex(a, b, c, **kw):
    pass


def more_complex(a, b, c, *other, **kw):
    print(a, b, c)
    print(other)
    print(kw)


def test_long():
    long(1, 3, 5)
    long(1, 3, 5, 6, 7)
    greet(name="Name")
    hello(b=3, a=1)
    kw(anders=1, mapp=2)
    too_complex(c=1, b=3, a=4, loops=3)
    more_complex(1, 2, 3, 4, 5, 6, zero=1)
