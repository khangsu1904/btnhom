string=str(input())
Sn=''
n=len(string)
for i in range(n-1,-1,-1):
    Sn=Sn+string[i]
if(Sn==string):
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not a palindrome.')
