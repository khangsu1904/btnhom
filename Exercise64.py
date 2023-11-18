cost = 0
while True:
    price= input('Enter the price (press Enter for the total):')
    if not price:
        break
    try:
       p = float(price)
       totalcost += p
    except ValueError:
       print('Please enter a valid number.')
cash =round(totalcost*100)  
remainder=cash % 5
if remainder < 2.5:
    cash += (5 - remainder)
print("\nTotal cost:",round(totalcost,2) )
print("Amount due for cash payment: ",round(cash/100, 2))
