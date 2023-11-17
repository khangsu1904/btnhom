user_input = input("Enter a string: ")
cleaned_input = ''.join(char.lower() for char in user_input if char.isalnum())
is_palindrome = True
length = len(cleaned_input)
for i in range(length // 2):
    if cleaned_input[i] != cleaned_input[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"The string '{user_input}' is a palindrome, ignoring spaces, punctuation, and case!")
else:
    print(f"The string '{user_input}' is not a palindrome, ignoring spaces, punctuation, and case.")
