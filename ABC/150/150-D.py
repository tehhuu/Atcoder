import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

N, M = map(int,input().split())
A = list(map(int,input().split()))

a = gcd(*A)
print(a)
for i in range(a, M+1,a*2):
    #print(i)
    i = float(i)
    flag = 0
    for j in A:
        #print((i / j)-0.5)
        if ((i / j)-0.5).is_integer() == False:
            flag = 1
    if flag == 0:
        print(i)
    
print('A')
