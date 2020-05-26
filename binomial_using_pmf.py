''' We can explicitly describe the probabilities in a Binomial Distribution '''

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

# print(binomial_pmf(15, 4, 0.7))

def binomial_dict(n, p=0.5):
    d = {}
    for k in range(0, n+1):
        d[k] = binomial_pmf(n, k, p)

    return d

# print(binomial_pmf(15, 4, 0.7))
sum = 0
for i in range(2,9):
    sum += binomial_pmf(15, i, 0.7)
#print(sum)
#breakout:4
##print(binomial_pmf(100,25,(1/3)))
#breakout:5
# print(binomial_pmf(3,1,0.68))
sum2=0
for i in range(1,4):
    sum2 += binomial_pmf(3,i,0.68)
# print(sum2)
# print(binomial_pmf(3,0,0.68))


# d = binomial_dict(20, 0.3)

# for k, v in d.items():
#     # print(f'{k}: {"*" * int(v*160)}')
#     print(f'{k}: {v}')

def num_crt_thr(thr, p=0.68):
    sum_=0
    num = 1
    while 1:
        for _ in range(num):
            sum_ += binomial_pmf(num,i,p)
            if sum_ > thr:
                return num
            else:
                num += 1
                
print(num_crt_thr(0.9))