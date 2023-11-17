x = float(input("Enter a number: "))
guess = x / 2
while abs(guess * guess - x) > 1e-12:
    guess = (guess + x / guess) / 2
print(f"The square root of {x} is approximately {guess}")
