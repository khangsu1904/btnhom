pi_approx = 0
for term in range(15):
    if term == 0:
        pi_approx += 3
    else:
        sign = (-1)**(term+1)
        a = 2*term        
        den = (a)*(a+1)*(a+2)
        pi_approx += (sign)*(4/den)       
    print(pi_approx)
