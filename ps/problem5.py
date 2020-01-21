freq = {}

def reduce_by_factor(number,factor):
	count = 0
	cur_num = number
	while cur_num % factor == 0:
		cur_num /= factor
		count += 1
	if factor in freq:
		if freq[factor] < count:
			freq[factor] = count
	elif count > 0:
		freq[factor] = count
	return cur_num

def populateFactors(x):
	cur_num = reduce_by_factor(x, 2)
	factor = 3
	while cur_num != 1:
		cur_num = reduce_by_factor(cur_num, factor)
		factor += 2
		
for r in range (2,21):
	populateFactors(r)
	
total = 1
for key,value in freq.items():
	total *= (key ** value)

print(total)