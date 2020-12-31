
# Python3 program to print a fraction  
# in Egyptian Form using Greedy 
# Algorithm 
  
# import math package to use 
# ceiling function 
import math 
import decimal
from decimal import Decimal


# define a function egyptianFraction  
# which receive parameter nr as 
# numerator and dr as denominator 
def egyptianFraction(nr, dr): 
    # enable large number support
    decimal.getcontext().prec = 100000000
    nr = Decimal(nr)
    dr = Decimal(dr)

    print(f"The Egyptian Fraction Representation of {nr}/{dr} is") 

  
    # empty list ef to store 
    # denominator 
    ef = [] 
  
    # while loop runs until  
    # fraction becomes 0 i.e, 
    # numerator becomes 0 
    while nr != 0: 
        
        x = Decimal(0)
        # taking ceiling 
        x = math.ceil(dr / nr) 
  
        # storing value in ef list 
        ef.append(x) 
  
        # updating new nr and dr 
        nr = Decimal(x * nr - dr)
        dr = Decimal(dr * x) 
  
    # printing the values 
    for i in range(len(ef)): 
        if i != len(ef) - 1: 
            print(f" 1/{ef[i]} +", end="") 
        else: 
            print(f" 1/{ef[i]}") 
  
# calling the function
alist = [[121, 48], 
        [1749257, 652080]]
for nr, dr in alist:
    egyptianFraction(nr, dr)

# This code is contributed  
# by Anubhav Raj Singh 
