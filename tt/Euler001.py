#Euler 1

total = 0

for r in range(1,1000,1):
	if r%3==0:
		total += r
	elif r%5==0:
		total += r

print (total)