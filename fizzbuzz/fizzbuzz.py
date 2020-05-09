def fizzbuzz(num):
    response = ''
    if (num % 3 == 0) and (num % 5 == 0):
        response = 'fizzbuzz'
    elif num % 3 == 0:
        response = 'fizz'
    else:
        response = 'buzz'
    return response