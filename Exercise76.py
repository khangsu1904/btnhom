n=int(input('Enter an integer (2 or greater): '))
factor=2
if n<2:
    print('Error!')
else:
    while factor<=n:
        if n%factor==0:
            print(factor)
            n/=factor
        else:
            factor=factor+1
