from oddint import isOdd

def test_one_integer():
    num_list = [7]
    assert isOdd(num_list) == 7

def test_two_integer():
    num_list = [0]
    assert isOdd(num_list) == 0