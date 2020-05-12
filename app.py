from fizzbuzz.fizzbuzz import fizzbuzz


exit_status = ''
while exit_status is not 'q':
    user_number = int(input('\nPlease type in a number: '))
    print(f'Output: {fizzbuzz(user_number)}\n')
    exit_status = input('Type any key to continue. Hit q to quit. ')
