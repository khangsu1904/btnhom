total = 0
count = 0

value = float(input("Enter a value (0 to end): "))

if value == 0:
    print("Error: The first value cannot be 0.")
else:
    while value != 0:
        total += value
        count += 1
        value = float(input("Enter a value (0 to end): "))

    average = total / count
    print(f"The average of the entered values is: {average}")
