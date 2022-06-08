import math
import gmpy2
import random
from time import time


def pollard_p1(n):
    A = random.randint(2, n - 1)
    gcdA = math.gcd(A,n)
    if (gcdA > 1 and gcdA < n):
        return gcdA
    
    k = 2

    iterations = 0
    start = time() 

    while True:
        iterations += 1
        A = pow(A, k, n) 
        d = math.gcd(int(A-1), n)
    
        if(d > 1 and d < n):
            print("___ FACTOR FOUND ___")
            print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))
            print(n, ", ", d, ", ", iterations, ", ", time() - start, sep='')
            return d
        if (d == n):
            print("___ NO FACTOR FOUND ___")
            print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))
            print(n, ", ", n, ", ", iterations, ", ", time() - start, sep='')
            return False
        k += 1

    
n = 644466866774061586188803

print("*** POLLARD P - 1 ***")
print("To factorize: ", n)
A = pollard_p1(n)

print("Factor found: ", A, sep='')

