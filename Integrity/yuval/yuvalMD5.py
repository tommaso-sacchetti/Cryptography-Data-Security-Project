from Crypto.Hash import MD5
from time import time
import random

from guppy import hpy

h = hpy() 

print(h.heap())

print("Collision test\n", "=*="*5)
messageL = "Legitimate message"
messageI = "Illegitimate message"

print("Legitimate message: " + messageI)
print("Illegitimate message: " + messageL)

messageL = messageL + "%d"
messageI = messageI + "%d"

messageL = messageL.encode("ascii")
messageI = messageI.encode("ascii")

places = input("To how many places of MD5? ")
places = int(places)

print("\n\n\n")

modificationsLegitimate = {}

finalMessageI = ''
finalMessageL = ''
finalHashI = ''
finalHashL = ''

# tableSize = 2^(HASHSIZE / 2)
tableSize = pow(2, places / 2)
tableSize = int(tableSize) # convert tableSize in int

for i in range(tableSize):
    collision = False
    hL = MD5.new(messageL % i) # the modifications of the hashed message are made through '%' operator and an int that increments every time
    xL = hL.hexdigest()[:places] # returns the first i bits of the hash (using everything would be too expensive, in hexadecimal form 
    modificationsLegitimate.update({messageL % i : xL})
    # DEBUG:
    # print(str(messageL % i) + x)

j = 0 # index for iterations
start = time()

while not collision:
    hI = MD5.new(messageI % j) # Modifications of illegitimate message
    xI = hI.hexdigest()[:places]
    for i in range(len(modificationsLegitimate)):
        if xI == modificationsLegitimate.get(messageL % i):
            collision = True
            finalMessageL = messageL % i
            finalMessageI = messageI % j
            finalHashI = xI
            finalHashL = modificationsLegitimate.get(messageL % i)

    j += 1

print("Total Attempts: %s / Took %0.2f seconds" %(j, time() - start))
print("Legitimate message: " + str(finalMessageL))
print("Illegitimate message: " + str(finalMessageI))
print("Hash: " + finalHashI)
print("Hash: " + finalHashL)
# print("Complete Hash: " + )


    







