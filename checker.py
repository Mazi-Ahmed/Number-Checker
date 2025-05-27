## Even Checker
number = int(input('Even Checker. Enter a number? '))

if number%2 == 0:
    print (number,'is an even number')
else:
    print( number, 'is an odd number')

## Odd Checker
def is_odd(n):
    return n%2 != 0

print (is_odd(4))

