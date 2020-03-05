#Euler 12 - What is the value of the first triangle number to have over five hundred divisors

fac_list = {}

def next_tri (y):
    tri = int((y*(y+1)/2))
    return (tri)

def prime_fac(num):
    global fac_list
    count = 0
    while num % 2 == 0:
        num /= 2
        count += 1
    fac_list[2] = count

    div_by = 3
    while num != 1:
        count = 0
        while num % div_by == 0:
            num /= div_by
            count += 1
        fac_list[div_by] = count
        div_by += 2

num = 1
tot_div = 0
while tot_div < 500:
    cur_tri = next_tri(num)
    prime_fac(cur_tri)
    
    tot_div = 1
    for key,value in fac_list.items():
        tot_div *= (value+1)
    
    if (tot_div > 500):
        print (cur_tri,": ",fac_list)
        print (tot_div)

    num += 1
    fac_list = {}