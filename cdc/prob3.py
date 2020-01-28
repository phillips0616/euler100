import math

end = 600851475143
factors = []

factor = 2
while factor < math.ceil((end/2) + 1):
    if end % factor == 0:
        end /= factor
        if factor not in factors:
            factors.append(factor)
    else:
        factor += 1
factors.append(end)   

print(end)
