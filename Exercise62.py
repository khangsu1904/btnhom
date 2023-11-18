print("Original Price   |   Discount Amount   |   New Price")
print('---------------------------------------------------')
P =  [4.95, 9.95, 14.95, 19.95, 24.95]
DP = 60
for i in P:
    DA = i*(DP/100)
    NP= i - DA
    DA= round(DA,2)
    NP= round(NP,2)
    print(f"${i:<17.2f} | ${DA:<19.2f} | ${NP:<11.2f}")
