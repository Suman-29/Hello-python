
# coding: utf-8

# In[ ]:

'''Use the formula

Pn = P0*(1+r)^n

where P0 is the principal amount, Pn is the compounded principal, 
r is the rate of interest and n is the number of year.

Assume r = 10% and n = 1 to 20, create a Python list that will store 
the value of (1+r)^n where n = 1 to 20. Subsequently, take an input from 
the command line for the value of P0 and calculate Pn all values of n. 
Repeat this process until a 'Q' or 'q' is pressed to quit the program.'''

# Calculate Compounded principal for years 1 to 20 with diff values of principal 
# rate = 10%
r = 10
#List comprehension to calculate the interest from 1 to 20 years
InterestLt=[((float(1+r/100.0))**n) for n in range(1,21)]

print ('\nFollowing is the list of interest calculated for 1 to 20 years:\n')
print (InterestLt)

while True:
    P0str = raw_input("\nPlease enter the principal amount: ")
    P0str.strip()
    if not P0str:
        print ("Enter some value")
    elif (P0str!='q') and (P0str!='Q'):
        try:
            P0=float(P0str)
        except:
            print("That's not a valid number")
            continue
        Pn = [P0*items for items in InterestLt]
        print ("\nBelow is the list of Compounded principal for 1 to 20 years for principal {}:\n".format(P0))
        print (Pn)
    else:
        print("User has quit")
        break
        

