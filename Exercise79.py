

num=int(input())
max_num = randrange(1, num + 1)
print(max_num)

updates = 0

for i in range(1, num):
    current = randrange(1, num + 1)
    if current > max_num:
        max_num = current
        updates += 1
        print('{}   <= Update'. format(current))
    else:
        print(current)

print('The maximum number found was', max_num)
print('The maximum number was updated {} times'. format(updates))