#Euler 2 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

total = 0
prev  = 1
cur   = 2

while cur < 4000000:
	if cur%2==0:
		total += cur
	cur += prev
	prev = (cur-prev)
print ("Total : "+str(total))