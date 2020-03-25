from decimal import *
getcontext().prec = 7000
#import numpy as np

a, b, c = map(float, input().split())

##print(a**0.5, b**0.5, c**0.5)
if Decimal(a).sqrt()+ Decimal(b).sqrt() < Decimal(c).sqrt():
    print('Yes')
else:
    print('No')

#if 2*((a*b)**0.5) < c - a - b:
    #print('Yes')
#else:
    #print('No')

'''
if float(np.sqrt(a))+float(np.sqrt(b)) < float(np.sqrt(c)):
    print('Yes')
else:
    print('No')]
'''