#Euler 5 - The smallest positive number that is evenly divisible by all of the numbers from 1 to 20

int_list = []
num = 1

def prime_check (z):
    if z >= 0 and z <=3:
        return True
    else:
        for y in range (2,int(z**0.5)+1,1):
            #print (str(z)+"%"+str(y)+" - "+str(z%y))
            if z%y==0:
                return False
        return True

for x in range (2,21,1):
    if prime_check(x)==True:
        w = x
        while w*x < 20:
            w *= x
        int_list.append(w)

for v in int_list:
    num *= v

print(int_list)
print (num)