solution = 0

def check_multiples(a,b,c):
    global solution
    prod = a + b + c

    if 1000 % prod != 0:
        return False

    factor = 1
    while prod < 1000:
        factor += 1
        prod = (a * factor) + (b * factor) + (c * factor)
    if prod == 1000:
        solution = (a * factor) * (b * factor) * (c * factor)
        return True
    return False

m = 2
n = 1
while solution == 0:
    for r in range(m,498):
        a = (r ** 2) - (n ** 2)
        b = 2 * r * n
        c = (r ** 2) + (n ** 2)
        if check_multiples(a,b,c):
            break
    n += 1
    m = n + 1

print("Solution: " + str(solution))

