print("Celsius   =>   Fahrenheit")
print('-------------------------')
for C in range (0,101,10):
    F = C*(9/5) + 32
    print(f"{C:^9} | {F:^12.2f}")
