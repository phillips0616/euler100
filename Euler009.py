#Euler 009 - There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc.

z = 4
a = 0
b = 0
c = 0
total  = 0
factor = 0

while z <= 332:
    a = z
    if a%2==0:
        b = ((a/2)**2)-1
        c = ((a/2)**2)+1
    else:
        b = ((a**2)/2)-0.5
        c = ((a**2)/2)+0.5
    total  = a+b+c
    factor = 1

    while total <= 1000:
        #print (total,'(',factor,')')
        if total == 1000:
            a *= factor
            b *= factor
            c *= factor
            z = 999
            break
        else:
            total  += a+b+c
            factor += 1
    z += 1

print (a,"+",b,"+",c," = ",total)
print (a*b*c)