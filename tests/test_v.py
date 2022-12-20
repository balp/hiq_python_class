import my_helper
from extras import names, increase, get
from extras import some_starange_name as my_names
import longer_name_that_i_like_to_use as ln

glob = 1


def test_scope():
    local = 1
    local = glob

    def func():
        l2 = local


def test_module():
    print(my_helper.greeting())
    for name in names():
        print(name)
    for name in my_names():
        print(name)
    for name in ln.some_name():
        print(name)


def test_adder():
    increase(3)
    assert get() == 5


def test_hiq():
    import hiq.xmas
    assert hiq.xmas.greeting("Simona") == 'God Jul, Simona.'
