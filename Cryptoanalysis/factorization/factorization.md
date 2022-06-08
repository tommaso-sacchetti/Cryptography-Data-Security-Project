# Factorizacion de enteros

The algorithm considered in this document are three: <code>fermat.py</code>, <code>pollard_rho.py</code> and <code>pollard_p-1.py</code>.

The machine in which they ran is a Macbook Pro with a 16 GB 3733 MHz LPDDR4X memory and a 2 GHz Intel Core i5 quad-core processor.

### POLLARD RHO

The <code>pollard_rho.py</code> algorithm is composed by a single cycle in which all the computations are performed. The algorithm performance could be improved by utilizing very optimized functions to elevate numbers to power and to find the gcd.

The algorithm has been tested with various number. The biggest it got tested with is <code>193511914779620529059179024576083896131</code> which is a 128 bit integer and the output is :

<code>*** POLLARD RHO ***<br>
Number to factorize:  <br>193511914779620529059179024576083896131<br>
___ NO FACTOR FOUND ___<br>
Total Iterations: 126823776 / Took 304.16 seconds<br>
Factor: 193511914779620529059179024576083896131<br></code>

The execution with a 64 bit integer such as an example <code>9916239399178531379</code> took 20.04 seconds and foud as a factor <code>3307524691</code>.


## POLLARD P-1
The implementation of the Pollard p-1 algorithm is straight forward. The only problem found during the development was the <code>mat.pow()</code> function of python that would overflow with very big numbers. It has been substituted with <code>pow(A, k, n)</code> that deals already with the module.

The execution with a 64 bit integer such as <code>9916239399178531379</code> took 5.406 seconds and foud as a factor <code>3307524691</code> with 975670 iterations. A drastic difference from the Pollard Rho algorithm, four times less

with the 80 bit number <code>644466866774061586188803</code> the algorithm found the factor <code>852015736981</code> in 37.38 seconds and 6220000 iterations.

The Pollard p-1 though couldn't solve higher size problems, such as the 128 bit integer <code>197628881444442442728148135740402563449</code>, in opposition of the Pollard Rho algorithm. The reason is probably the very big raise to power at the beginning. Although when it can solve the problem, Pollard p-1 is significantly faster

## FERMAT
In the Fermat algoritm the library <code>gmpy2</code> has been used due to its optimization and for faster computation of the root of the numbers.

The algorithm has been tested with the 64 bit integer <code>9916239399178531379</code>. Output: 

> <code>*** FERMAT ***<br>
To factorize:  9916239399178531379<br>
Total Iterations: 5957768 / Took 14.59 seconds<br>
Factors found: 2961166042, 3348761690<br></code>

But with bigger numbers, such as <code>197628881444442442728148135740402563449</code> the algorithm breaks, in particular in the computation of the square root.