m=int(input())
n=int(input())
d = min(n, m)
while m % d != 0 or n % d != 0:
    d -= 1
print(f'The greatest common divisor of {m} and {n} is: {d}')   
    
