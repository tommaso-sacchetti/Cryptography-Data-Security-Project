# Arcoiris Algorithm

The implementation of the algorithm is composed of two parts: <code>rainbow.py</code> and <code>rainbow_attack.py</code>.
The first script builds the rainbow table while the second attacks it. They share parameters such as the password size, the number of records and the hash size.

As has function a truncated to n bits MD5 was selected.

During the test different table sizes has been tried and the only one that could bring to a result was a 50000 record table with sequences of 10 values.

The algorithm could find collisions only in case of a 3 characters password and hash. The considered passwords are alphanumeric passwords and the function of decoding the hash is simply the first characters of the hash, used as password.

The output of a test with three characters is the following: 
> <code>Password hash:  47b<br>
position: 2627<br>
root password: vzq<br>
first hash: eee<br>
PASSOWRD FOUND!<br>
        Password found: b51 Colliding hash: 47b | Real password: aaa<br>
Total Iterations: 9 / Took 0.02 seconds<br></code>

The machine in which the script ran is a Macbook Pro with a 16 GB 3733 MHz LPDDR4X memory and a 2 GHz Intel Core i5 quad-core processor.