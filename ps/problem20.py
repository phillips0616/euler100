
def fac(n, result):
    if n == 1:
        return result
    else:
        return fac(n-1, result*n)
print(sum([int(x) for x in str(fac(100,1))]))