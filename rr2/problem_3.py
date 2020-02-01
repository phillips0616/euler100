""" Project Euler - Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

factors = []
primes = []

num = 600851475143

for i in range(2, num + 1):
    primes.append(i)

i = 2

while(i <= int(math.sqrt(num))):
    if i in primes:
        for j in range(i * 2, num + 1, i):
            if j in primes:
                primes.remove(j)
    i += 1

for x in primes:
    if num % x == 0:
        factors.append(x)

print(factors[-1])