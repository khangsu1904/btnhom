import math

total_perimeter = 0

print("Enter the x part of the coordinate: ", end='')
x_prev = float(input())

print("Enter the y part of the coordinate: ", end='')
y_prev = float(input())

while True:
    print("Enter the x part of the coordinate (blank to quit): ", end='')
    x_input = input()

    if not x_input:
        break  

    x_current = float(x_input)

    print("Enter the y part of the coordinate: ", end='')
    y_current = float(input())
