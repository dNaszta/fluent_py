from array import array
from random import random

number_of_randoms = 10**7
floats = array('d', (random() for i in range(number_of_randoms)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fe = open('floats.bin', 'rb')
floats2.fromfile(fe, number_of_randoms)
fe.close()
print(floats2[-1])
print(floats == floats2)
