#Euler 16 - What is the sum of the digits of the number 2**1000?

z = str(2**1000)
sum = 0

for y in range(len(z)):
    sum += int(z[y])

print(z)
print(sum)