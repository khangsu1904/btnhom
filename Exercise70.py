message = input("Enter the message i.e to be decrypted: ").strip()   
letters="abcdefghijklmnopqrstuvwxyz"
Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k = int(input("Enter the key to decrypt: "))
shifted_message = ""
for ch in message:
    if ch in letters:
        position = letters.find(ch)
        new_pos = (position + k) % 26
        new_char = letters[new_pos]
        shifted_message += new_char
    else:
        shifted_message += ch
Shifted_message=""       
for char in shifted_message:
    if char in Letters:
        Position = Letters.find(char)
        New_pos = (Position + k) % 26
        New_char = Letters[New_pos]
        Shifted_message += New_char
    else:
        Shifted_message += char
print("The shifted message is:\n")
print(Shifted_message)
