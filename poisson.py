def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

def poisson_pmf(lmb, k):
    return (lmb**k) *(2.71828**(-lmb))/fact(k)

def poisson_pmf_dict(lmb, low_k, high_k):
    dict_ = dict()
    for i in range(low_k, high_k + 1):
        dict_[i] = poisson_pmf(lmb, i)
    
    return dict_

d = (poisson_pmf_dict(10,0,20))

for k, v in d.items():
    print(f"{k}:{int(v*380)*'*'}")