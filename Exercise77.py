binary=input('Enter binary number (base 2): ')
decimal = 0
for i in binary:
    decimal = int(i) + decimal * 2
print(f'{binary} in binary into decimal is {decimal}')
