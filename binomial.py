#from scipy.stats import binom

# 5 successes 20 tial p=0.3

def factorial(n):
    prod=1
    for num in range(1, n+1):
        prod *= num
    
    return prod

def combinations(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

def binomial_pmf(n, k, p):
    return combinations(n, k) * p**k * (1-p)**(n-k)

# print(binomial_pmf(20, 5, 0.3))

def binomial_dict(n, p=0.5):
    
    d = {}
    for k in range(0, n+1):
        d[k] = binomial_pmf(n, k, p)

    return d

d = binomial_dict(20, 0.3)

for k,v in d.items():
    print(f'{k}: {"*" * int(1e2*v)}')