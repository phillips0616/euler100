""" Project Euler - Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples_sum(num):
    sum = 0
    for x in range(num):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
            print(x)
    print(sum)


multiples_sum(1000)