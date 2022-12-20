from make_roman import to_roman
import pytest


# Test lista:
#
#   1 -> I
#   2 -> II
#   4 -> IV
#   5 -> V
#   6 -> VI
#   9 -> IX
#  10 -> X
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

@pytest.mark.parametrize("number, expected", [
    (1, 'I'),
    (2, 'II'),
    (4, 'IV'),
    (5, 'V'),
    (10, 'X'),
    (19, 'XIX'),
    (23, 'XXIII'),
    (35, 'XXXV'),
    (40, 'XL'),
    (44, 'XLIV'),
    (90, 'XC'),
    (50, 'L'),
    (94, 'XCIV'),
    (111, 'CXI'),
    (457, 'CDLVII'),
    (557, 'DLVII'),
    (902, 'CMII'),
    (1555, 'MDLV'),
    (1994, 'MCMXCIV'),
    (2022, 'MMXXII'),
])
def test_roman(number, expected):
    assert to_roman(number) == expected
