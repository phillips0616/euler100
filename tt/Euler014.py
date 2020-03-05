#Euler 14 - Which starting number, under one million, produces the longest chain in the collatz sequence?

seq_totals = {}
x = 1
cur = 1
high = 1
start = 1

def col_seq_count(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num *= 3
            num += 1
            count += 1
        if num in seq_totals:
            count += seq_totals[num]
            return (count)
    return (count)



while x < 1000000:
    cur = col_seq_count(x)
    
    seq_totals[x] = cur

    if high < cur:
        high = cur
        start = x
    
    x += 1

print (len(seq_totals))
print (start," :  ",high)