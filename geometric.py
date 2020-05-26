def geometric_pmf(p, k):
    '''
     p: probability of success
     k: number of trials before success
     Output:
        probability of success after k trials
    '''
    return ((1-p)**k) * (p)

def geometric_cdf(p, k):
    return 1 - ((1-p)**(k+1))

def geometric_cdf_(p, k):
    sum_=0
    for r in range(k+1):
        sum_ += geometric_pmf(p, r)

    return sum_

def geometric_pmf_dict(p, k):
    d = dict()

    for r in range(k+1):
        d[r] = geometric_pmf(p, r)

    return d

# d = (geometric_pmf_dict(0.5, 10))

# for k, v in d.items():
#     print(f"{k}:{v}")


def geometric_cdf_dict(p, k):
    d = dict()

    for r in range(k+1):
        d[r] = geometric_cdf(p, r)

    return d

# d = (geometric_cdf_dict(0.5, 10))

# for k, v in d.items():
#     print(f"{k}:{v}")

from random import random

def bernoulli_trial(p):
    if random() < p:
        return 1
    else:
        return 0

# print(bernoulli_trial(0.3))

def geometric(p=0.5):
    n = 1
    while True:
        if bernoulli_trial(p):
            return n - 1
        else:
            n+=1

# print(geometric(p=0.05))

def geometric_samples_dict(p, num_samples):
    d = dict()

    for _ in range(num_samples):
        k = geometric(p)
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

    return d

# d = geometric_samples_dict(p=0.3, num_samples=10000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

def geometric_samples_prob_dict(p, num_samples):
    d = dict()

    for _ in range(num_samples):
        k = geometric(p)
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

    new_d = dict()

    for k, v in d.items():
        new_d[k] = v / num_samples

    return new_d

d = geometric_samples_prob_dict(p=0.3, num_samples=10000)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')