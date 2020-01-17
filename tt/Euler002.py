#Euler 2 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

total = 0
prev  = 1
cur   = 2

for x in range(32):
	if cur < 4000000:
		#print (cur)
		if cur%2==0:
			total += cur
		cur += prev
		prev = (cur-prev)
	#else:
		#print ("Loop No. "+str(x))
print ("Total : "+str(total))