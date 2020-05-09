def fizzbuzz(num):
    response = ''
    if (num % 3 == 0) and (num % 5 == 0):
        response = 'fizzbuzz'
    elif num % 3 == 0:
        response = 'fizz'
    elif num % 5 == 0:
        response = 'buzz'
    else:
        response = num
    return response