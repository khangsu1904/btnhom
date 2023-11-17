result = ""
q = int(input("Enter a decimal number: "))
while q!=0:
    r=q%2
    result=result +str(r)
    q//=2
print(result)
