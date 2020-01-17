#Euler 1 - Find the sum of all the multiples of 3 or 5 below 1000.

total = 0

for r in range(1,1000,1):
	if r%3==0:
		total += r
	elif r%5==0:
		total += r

print (total)