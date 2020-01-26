ceiling = 2000000
def sieve_of_eratosthenes (ceiling):
    values = [True] * ceiling 
    for r in range(2, int(ceiling ** 0.5) + 1):
        if values[r] == True:
            for j in range(r*r, ceiling, r):
                values[j] = False
    primes = [r for r in range(ceiling) if values[r] == True]
    return primes[2:]

solution = sum(sieve_of_eratosthenes(ceiling))

print(solution)