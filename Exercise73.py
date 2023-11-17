import string
def is_palondrome(s):
    s=''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
phrase = input('Enter a phrase: ')
if is_palondrome(phrase):
    print(f'{phrase} is a palindrome!')
else:
    print(f'{phrase} is not a palindrome.')
