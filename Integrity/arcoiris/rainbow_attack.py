from Crypto.Hash import MD5
from time import time
import random
import string

SEQUENCE_LENGTH = 10
ENTRY_SIZE = 50000
PASSWORD_SIZE = 3
HASH_SIZE = 3

def decode(hash):
    return hash

def exists(table, hash):
    for i in range(len(table)):
        if hash == table[i][1]:
            return i
    return -1

PASSWORD="aaa"
HASH=MD5.new(PASSWORD.encode("ascii")).hexdigest()[:HASH_SIZE]

print("Password hash: ",HASH)


file = open("rainbow_table.txt", "r")

table = []

t = SEQUENCE_LENGTH
n = ENTRY_SIZE

k = 0
for line in file:
    table.append(line.strip().split(' '))
    k += 1

p = HASH

iterations = 0
start = time()

for i in range(1, t+1):
    iterations += 1
    position = exists(table, p)
    if(position >= 0): 
        print("position: " + str(position))
        break
    temp_password = decode(p)
    temp_password = temp_password.encode("ascii")
    p = MD5.new(temp_password).hexdigest()[:HASH_SIZE]

if i != t:
    password = table[position][0]
    print("root password: " + password)

    password = password.encode("ascii")
    new_hash = MD5.new(password).hexdigest()[:HASH_SIZE]
    print("first hash: " + new_hash)

    while new_hash != HASH:
        iterations += 1
        password = decode(new_hash)
        password = password.encode("ascii")
        # print(password)
        new_hash = MD5.new(password).hexdigest()[:HASH_SIZE]

    password = password.decode("ascii")
    print("PASSOWRD FOUND!\n\tPassword found: " + password + " Colliding hash: " + HASH + " | Real password: " + PASSWORD)

    print("Total Iterations: %s / Took %0.2f seconds" %(iterations, time() - start))


if(i == t):
    print("NO PASSWORD FOUND...")

