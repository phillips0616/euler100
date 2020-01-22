#Euler 6 - Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

s_sq = 0
sq_s = 0

for z in range (1,101,1):
    s_sq += z**2
    sq_s += z
    #print (s_sq)
    print (sq_s)

sq_s = sq_s**2

print (sq_s,"-",s_sq," = ",sq_s-s_sq)