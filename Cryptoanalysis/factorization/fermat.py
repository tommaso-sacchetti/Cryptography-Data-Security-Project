import math
import gmpy2
from time import time


def perfect_square(n):
    root = gmpy2.root(n,2)
    if(root%1 > 0):
        return False
    return True


def fermat(n):
    A = math.ceil(gmpy2.root(n,2))
    B = math.pow(A, 2) - n

    start = time()
    iterations = 0
    while not perfect_square(B):
        iterations += 1
        A += 1
        B = math.pow(A, 2) - n

    B_root = gmpy2.root(B,2)
    print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))
    return (int(A-B_root), int(A+B_root))

n = 197628881444442442728148135740402563449

print("*** FERMAT ***")
print("To factorize: ", n)
A, B = fermat(n)

print("Factors found: ", A, ", ", B, sep='')


