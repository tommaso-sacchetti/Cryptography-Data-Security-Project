import math
import gmpy2
import random
from time import time


def pollard_rho(n):
    A = random.randint(2, n - 1)
    B = A

    start = time()
    iterations = 0
    while True:
        iterations += 1
        A = (math.pow(A, 2) + 1) % n 
        B = (math.pow(B, 2) + 1) % n 
        B = (math.pow(B, 2) + 1) % n 
        # print(A, B) 
        p = math.gcd(int(A - B), n)
    
        if(p > 1 and p < n):
            print("___ FACTOR FOUND ___")
            print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))
            print(n, p, time() - start)
            return p
        if (p == n):
            print("___ NO FACTOR FOUND ___")
            print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))
            print(n, p, time() - start)
            return n

    
n = 644466866774061586188803

print("*** POLLARD RHO ***")
print("Number to factorize: ", n)

A = pollard_rho(n)

print("Factor: ", A, sep='')

