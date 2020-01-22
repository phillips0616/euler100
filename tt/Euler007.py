#Euler 7 - The 10,001st prime number

p_list = []
x = 0

def prime_check (z):
    if z >= 0 and z <=3:
        return True
    else:
        for y in range (2,int(z**0.5)+1,1):
            #print (str(z)+"%"+str(y)+" - "+str(z%y))
            if z%y==0:
                return False
        return True

while len(p_list) < 10001:
    if prime_check(x) == True:
        p_list.append(x)
    x += 1

print(len(p_list))
print (p_list[10000])