# Matthew Lund mtlund@wpi.edu
#DLP Challenge Baby-Step Giant-Step Algorithm

from math import ceil, sqrt #for math in bsgs
import time #for outputting execution time
import psutil #for looking @ memory usage
import os   #for accessing memory usage
import numpy #for addressing possible memory leak issues in table to limit to 32 bit (sqrt(P of 60 bits) = 30 bits)

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
    process = psutil.Process(os.getpid())
    base_memory_usage = process.memory_info().rss

    N = numpy.uint32(ceil(sqrt(p - 1)))  # phi(p) is p-1 if p is prime

    # Store hashmap of a^{1...N} (mod p). Baby step.
    tbl = {numpy.uint64(mod_exp(a, i, p)): numpy.uint32(i) for i in range(N)}

    #Report RAM utilization of Hashmap
    memory_usage = process.memory_info().rss
    table_memory_usage = memory_usage - base_memory_usage
    print((table_memory_usage * (10**-6)), 'MB of RAM used for Table Execution')

    # Precompute via Fermat's Little Theorem
    c = square_and_multiply(a, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (b * mod_exp(c,j,p)) % p    #modular exponention for y
        if y in tbl:    #check for y
            return j * N + tbl[y]


    # Solution not found
    return None
    
# Implementations

#40 bits implementation
a = 3
b = 1228035139812
p = 2199023255867

print('a: ', a, 'B: ', b,'P: ', p)
start = time.time()
x = bs_gs(a,b,p)
execution_time = time.time()
elapsed = execution_time - start
print('X =',x)
print('Execution Time (seconds):', elapsed)

print() #new line

#60 bits implementation
a = 3
b = 259893785866906004
p = 2305843009213699919
print(a, b, p)
start = time.time()
print('a: ', a, 'B: ', b,'P: ', p)
start = time.time()
x = bs_gs(a,b,p)
execution_time = time.time()
elapsed = execution_time - start
print('X =',x)
print('Execution Time (seconds):', elapsed)