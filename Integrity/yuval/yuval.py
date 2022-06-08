import zlib

""" To create a crc32 hash zlib will, be used, crc32 requires bits -> [Usage: bitstring = b'string']

s = b'message'

t = zlib.crc32(s)

print(t)
"""

"""In order to show the functioning of the algorithm, crc32 is gonna be used and messages will be composed by 8 integers, for the sake of simplicity in the excercise"""

messageL = b'12345678' 
messageI = b'11111111' 

HASHSIZE = 32 # crc32 is gonna be used for demonstration purpose

def yuval(messageL, messageI):
    """Looks for hash collisions using the yuval algorithm and the two messages
    
    @param messageL: legitimate message, a table of minor modifications is gonna be created, with their rispective hashes

    @param messageI: illegitimate message

    @return messageL1, messageI1: the two new messages with the hash collision
    """
    
    modificationsLegitimate = {}

    
    # tableSize = 2^(HASHSIZE / 2)
    tableSize = pow(2, HASHSIZE / 2)

    for i in range(int(tableSize)):
        message = messageL % i
        hashMessageL = zlib.crc32(messageL)
        modificationsLegitimate.update({messageL : hashMessageL})
        print(chr(messageL) + hashMessageL)
        

yuval(messageL, messageI)

hashed = zlib.crc32(messageL)
print(hashed)