from math import ceil, sqrt
import time
from multiprocessing import Pool


#modular exponention expression
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod

    return result

def bs_gs(a, b, p, N, tbl):

    # Precompute via Fermat's Little Theorem
    c = pow(a, N * (p - 2), p)

    def pow_mod(base, exp): #to call mod_exp in here
        return mod_exp(base, exp, p)
    
    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (b * pow_mod(c,j)) % p
        if y in tbl:
            return j * N + tbl[y]


    # Solution not found
    return None
    
# Solve for x


#40 bits implementation
a = 3
b = 1228035139812
p = 2199023255867
N = int(ceil(sqrt(p - 1)))  # phi(p) is p-1 if p is prime

# Store hashmap of g^{1...m} (mod p). Baby step.
tbl = {pow(a, i, p): i for i in range(N)}
print(a, b, p)
start = time.time()
x = bs_gs(a,b,p, N, tbl)
execution_time = time.time()
elapsed = execution_time - start
print(x)
print('Execution Time (seconds):', elapsed)

'''
#60 bits implementation
a = 3
b = 259893785866906004
p = 2305843009213699919
print(a, b, p)
start = time.time()
N = int(ceil(sqrt(p - 1)))  # phi(p) is p-1 if p is prime
tbl = [pow(a, i, p): i for i in range(N)]
print(a, b, p)
start = time.time()
x = bs_gs(a,b,p, N, tbl)
execution_time = time.time()
elapsed = execution_time - start
print(x)
print('Execution Time (seconds):', elapsed)
'''
