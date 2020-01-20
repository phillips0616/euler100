#Euler 3 - Largest prime factor of the number 600851475143


seed   = 600851475143
factor = seed
div_by = 2
plist  = "All prime factors: "

while factor%2 == 0:
	factor /= 2
	plist += str(div_by)+','
	print (factor)
	print (plist)

div_by = 3

while div_by <= factor/2:
	if factor%div_by == 0:
		factor /= div_by
		plist += str(div_by)+','
	else:
		div_by += 2

plist += str(factor)
print (plist)
print ("Largest prime factor: "+str(factor))