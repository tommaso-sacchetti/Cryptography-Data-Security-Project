# Logaritmo discreto
As algorithm for the computation of the discrete logarithm the baby step giant step was executed.

The algorithms works thanks to the application of Fermat's Little Theorem for the computation of the inverse modulo n.

The algorithm performs a fixated number of iterations which is n*(n-1) where n is the square root of p rounded up.

It computes the k of a 32 bit value <code>3326067959, alfa = 2, beta = 3039391640950870698</code> in 0.15 seconds.

A 64 bit value has been tested: <code>10682326048905763339</code>, alfa = 2, beta = 3039391640950870698</code> but the algorithm couldn't terminate the run and compute the result.

The machine in which it ran is a Macbook Pro with a 16 GB 3733 MHz LPDDR4X memory and a 2 GHz Intel Core i5 quad-core processor.