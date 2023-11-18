import random 
totalflips=0
for i in range(10):
    count = 0
    consecutive=0
    againresult=None
    while consecutive<3:
        result=random.randrange(2)
        count+=1
        if count>1:
            if result==againresult:
                consecutive+=1
            else:
                consecutive=1
        print('H ' if result==0 else 'T ', end='')
        againresult=result
    totalflips+=count
    print(f'({count} flips)')
avrflips = totalflips/10
print(f'On average, {avrflips} flips were needed')
