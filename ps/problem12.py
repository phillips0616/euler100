# This solutino is kind of slow...
# I am wondering if you can relate the factors of the previous triangle number to the next. That would speed it up.
freq = {}

def find_triag_num(n):
    return (n * (n+1)) / 2

def reduce_by_factor(number,factor):
    global freq
    count = 0
    cur_num = number
    while cur_num % factor == 0:
        cur_num /= factor
        count += 1
    freq[factor] = count
    return cur_num

def populateFactors(x):
	cur_num = reduce_by_factor(x, 2)
	factor = 3
	while cur_num != 1:
		cur_num = reduce_by_factor(cur_num, factor)
		factor += 2

x = 1
while True:
    num = find_triag_num(x)
    populateFactors(num)
    num_of_divisors = 1
    for key,value in freq.items():
        num_of_divisors *= (value + 1)
    if num_of_divisors > 500:
        print(num)
        break
    freq = {}
    x += 1

