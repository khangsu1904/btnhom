m=int(input())
n=int(input())
d = min(n, m)
while True:
    if not(n%d == 0 and m%d == 0):
        d-=1
    else:
        break
print(f'The greatest common divisor of {m} and {n} is: {d}')   
    
