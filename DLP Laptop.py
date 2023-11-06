# Matthew Lund mtlund@wpi.edu
#DLP Challenge Baby-Step Giant-Step Algorithm

from math import ceil, sqrt #for math in bsgs
import time #for outputting execution time

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

def square_and_multiply(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Square base and reduce exponent by half
        base = (base * base) % modulus
        exponent = exponent // 2

    return result

def bs_gs(a, b, p):

    N = int(ceil(sqrt(p - 1)))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(a, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = square_and_multiply(a, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (b * mod_exp(c,j,p)) % p    #modular exponention for y
        if y in tbl:    #check for y
            return j * N + tbl[y]


    # Solution not found
    return None
    
# Solve for x

#40 bits implementation
a = 3
b = 1228035139812
p = 2199023255867

print('a: ', a, 'B: ', b,'P: ', p)
start = time.time()
x = bs_gs(a,b,p)
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