# Busqueda de documentos alternativos

The python script <code>yuvalMD5.py</code> considers as hash function MD5 and since it's a very secure function only the first <code>n</code> characters of the resulting hash are considered, where <code>n</code> is provided by the user during runtime.

The algorithm finds a collision between two potential passwords in which the last character(s) gets modifyed.

The messages are strings with a variable attached in the end that gets modifyied every cycle. 
A more "intelligent" modification of the passwords could bring to big improvements in the algorithm's performances.

The algorithm has been tested with the first 3, 4, 5 and 6 characters of the MD5 hash. The search for the collision with 6 characters lasted 50.58 seconds, with 7874121 total attempts to find collision. The messages are <code>Legitimate message</code> and <code>Illegitimate message</code> and the colliding hash found is <code>bc9f03</code>.
The search with 5 characters lasts 0.04 seconds with 6782 iterations.
Finally the search with 7 characters took 36651669 in 256.49 seconds.

It's easy to note that the iterations and time increase exponentially with regards to the hash size


The machine in which the script ran is a Macbook Pro with a 16 GB 3733 MHz LPDDR4X memory and a 2 GHz Intel Core i5 quad-core processor.

