def is_palindrome(s):
    s= ''.join (char.lower() for char in s if char.isalnum())
    length = len(s)
    for i in range(length // 2):
        if s[i] !=s[length - i -1]:
            return False
    return True
user_input = input('Enter a string: ')
if is_palindrome(user_input):
    print(f'{user_input} is a palindrome!')
else: 
    print(f'{user_input} is not a palindrome.')
