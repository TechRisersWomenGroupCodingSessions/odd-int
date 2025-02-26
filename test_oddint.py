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
    num_list = [0,-1,0,-1,0]
    assert isOdd(num_list) == 0

def test_if_multiple_integers_returns_4():
    num_list = [1,2,2,3,3,3,4,3,3,3,2,2,1]
    assert isOdd(num_list) == 4

def test_non_valid_input():
    num_list = ['forty', 'two']
    assert isOdd(num_list) == 'Not valid input'

