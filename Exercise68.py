str = input("Enter a string of 8 bits: ")
while str != "":
    if str.count("1")+str.count("0") !=8 or len(str) != 8:
        print("Error")
    else:
        num = str.count("1")
        if num % 2 == 0:
            print("The parity bit should be 0")
        else:
            print("The parity bit should be 1")
    str = input("Enter 8 bits: ")
