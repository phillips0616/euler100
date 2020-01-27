#Euler 10 - Find the sum of all the primes below two million.

int_list = []
num = 0

def prime_check (z):
    if z >= 0 and z <=3:
        return True
    else:
        if z%2 == 0:
            return False
        for y in range (3,int(z**0.5)+1,2):
            #print (str(z)+"%"+str(y)+" - "+str(z%y))
            if z%y==0:
                return False
        return True

for x in range (3,2000000,2):
    if x==3:
        num += 1+2+3
        #int_list.append(1,2,3)
    elif prime_check(x)==True:
        num += x
        #int_list.append(x)

#print(int_list)
print (num)