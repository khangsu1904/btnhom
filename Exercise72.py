string=str(input())
a=''
n=len(string)
for i in range(n-1,-1,-1):
    a=a+string[i]
if(a==string):
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not a palindrome.')
