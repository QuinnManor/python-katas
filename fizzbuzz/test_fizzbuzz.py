from fizzbuzz import fizzbuzz


def test_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_buzz():
    assert fizzbuzz(5) == 'buzz'