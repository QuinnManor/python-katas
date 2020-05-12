def fizzbuzz(num):
    if is_fizzbuzz(num):
        response = 'fizzbuzz'
    elif is_fizz(num):
        response = 'fizz'
    elif is_buzz(num):
        response = 'buzz'
    else:
        response = num
    return response


def is_fizzbuzz(num):
    return (num % 3 == 0) and (num % 5 == 0)


def is_fizz(num):
    return num % 3 == 0


def is_buzz(num):
    return num % 5 == 0
