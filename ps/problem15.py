# observing a given path in a (NxN) grid shows you must move right N times and down N times
# This redues to a n choose k problem
# n!/((k!)*((n-k)!))

def calc_fac(n,m):
    if m == 1:
        return n
    else:
        return calc_fac(n*(m-1), m-1)

grid_size = 20

n = grid_size * 2
k = grid_size

n_fac = calc_fac(n,n)
k_fac = calc_fac(k,k)

print(n_fac / ((k_fac) * (k_fac)))

