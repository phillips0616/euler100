#Euler 4 - Find the largest palindrome made from the product of two 3-digit numbers.

z = 999
y = 999
x = 0
p = 0
floor  = 0
digit  = 0
length = 0
pal    = -1

while y >= floor:
	x = z*y
	length = len(str(x))
	digit = int(length/2)
	p=x
	#print(str(digit))
	for a in range (0,digit,1):
		print (str(z*y)+" - "+str(x)[a]+"  "+str(x)[length-a-1])
		if str(x)[a] != str(x)[length-a-1]:
			p = 0
			break
	if p > 0 and p > pal:
		#print (str(p))
		pal = p
		floor = y
		z -= 1
		y = z
	elif y == floor:
		z -= 1
		y = z
	else:
		y -= 1

print (str(z)+" x "+str(y))
print (str(pal))

for x in range (0,10,1):
	print(str(x))