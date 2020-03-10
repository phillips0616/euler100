#Euler 15 - Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.  How many such routes are there through a 20×20 grid?

import math

print (math.factorial(40)/(math.factorial(20)*math.factorial(20)))

def fac (z):
    total = 1
    for x in range(1,z+1,1):
        total *= x
    return (total)

print (fac(40)/(fac(20)**2))