def sieve_of_eratosthenes (ceiling):
    values = [True] * ceiling 
    for r in range(2, int(ceiling ** 0.5) + 1):
        if values[r] == True:
            for j in range(r*r, ceiling, r):
                values[j] = False
    primes = [r for r in range(ceiling) if values[r] == True]
    return primes[1:]

prime_list = sieve_of_eratosthenes(150000)
print(prime_list[10001])