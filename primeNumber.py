# getting number as input

input_number = int(input('Please enter a number: '))

if input_number > 1:
    for num in range(2, input_number):
        if input_number % num == 0:
            print('The number {} is not a prime number'.format(input_number))
            break
    else:
        print('The number {} is a prime number'.format(input_number))
else:
    print('The number {} is not a prime number'.format(input_number))
