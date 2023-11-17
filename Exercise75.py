def find_gcd(n, m):
    d = min(n, m)
    while d > 0:
        if n % d == 0 and m % d == 0:
            break
        d = 1
    return d 
num1 = int(input('Enter the first positive integer: '))
num2 = int(input('Enter the second positive integer: '))
gcd = find_gcd(num1, num2)
print(f'The greatest common divisor of {num1} and {num2} is: {gcd}')
