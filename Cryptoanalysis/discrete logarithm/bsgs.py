import math
from time import time

def babystep_giantstep(p, alfa, beta):
    n = math.ceil(math.sqrt(p))

    T = {}

    for r in range(n):
        key = pow(alfa, r, p)
        T[key] = r
    
    # Fermat's Little Theorem for the computation of inverse
    c = pow(alfa, n * (p-2), p)
    gamma = beta

    #print(T)

    for q in range(n-1):
        #print(gamma)
        if gamma in T:
            k = q*n + r
            return k
        gamma = pow(alfa*gamma, n * (p-2), p)
    

p, alfa, beta = 10682326048905763339, 2, 3039391640950870698
print("*** BABY STEP - GIANT STEP ***")
print("p, alfa, beta: ", p, alfa, beta )
start = time()
k = babystep_giantstep(p, alfa, beta)
#k = babystep_giantstep(487,33,303)


print("k found: ", k, sep='')
print("Excecutions time [s]: ", time() - start)

