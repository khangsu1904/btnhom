import random

updates=0

num=100
max=random.randrange(1,num+1)
print(max)
for i in range(1,num):
    current=random.randrange(1,num+1)
    if current>max:
        updates=updates+1
        max=current
        print(f'{max}  <== Update')
    else:
        print(current)
print(f'The maximum value found was {max}')
print(f'The maximum value updated {updates} times')
