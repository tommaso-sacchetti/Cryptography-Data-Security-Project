from Crypto.Hash import MD5
from time import time
import random
import string

"""
RAINBOW TABLE ATTACK

password info: 5 alphabetical lower case characters

hash algorithm used: MD5 truncated to 5 characters

"""

SEQUENCE_LENGTH = 10
ENTRY_SIZE = 50000
PASSWORD_SIZE = 3
HASH_SIZE = 3

table = []

t = SEQUENCE_LENGTH
n = ENTRY_SIZE
file = open("rainbow_table.txt", "w")

def generateRandomPassword(pSize) :
    password = ''
    for i in range(pSize):
        c = random.choice(string.ascii_lowercase)
        password += c
    return password

def decode(hash):
    return hash

for i in range(n) :
    row = []
    randomPassword = generateRandomPassword(PASSWORD_SIZE)
    password = randomPassword
    for j in range(1, t-1):
        password = password.encode("ascii")
        password =  decode(MD5.new(password).hexdigest()[:HASH_SIZE])

    password = password.encode("ascii")
    table.append( [randomPassword, MD5.new(password).hexdigest()[:HASH_SIZE]] )


for i in range(n):
    print(table[i])
    file.write(str(table[i][0]) + ' ' + str(table[i][1]) + '\n')




