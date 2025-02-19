from oddint import isOdd

def test_one_integer():
    num_list = [7]
    assert isOdd(num_list) == 7

def test_zero():
    num_list = [0]
    assert isOdd(num_list) == 0

def test_three_integers():
    num_list = [1,1,2]
    assert isOdd(num_list) == 2

def test_if_multiple_integers_returns_0():
    num_list = [0,1,0,1,0]
    assert isOdd(num_list) == 0