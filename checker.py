## Even Checker
# number = int(input('Even Checker. Enter a number? '))

# if number%2 == 0:
#     print (number,'is an even number')
# else:
#     print( number, 'is an odd number')

## Odd Checker
# def is_odd(n):
#     return n%2 != 0

# print (is_odd(4))

## Basic Calculator

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input('Enter operator: ')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('Invalid operator')

