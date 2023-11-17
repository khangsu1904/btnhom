def newtons_method_sqrt(x):
    guess = x/2.0
    threshold = 1e-12
    while abs( guess * guess - x ) > threshold:
        guess = ( guess + x / guess ) / 2.0
    return guess
user_number = float(input('Enter a number to find the square root: '))
if user_number < 0:
    print('Please enter a non-negative number')
else:
    result = newtons_method_sqrt(user_number)
    print (f'The square root of {user_number} is approximately: {result}' )   
