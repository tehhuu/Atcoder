'''import math
A, B = map(int, input().split())
print(A * B // math.gcd(A, B))
'''

import fractions
A,B=map(int, input().split())
f=fractions.gcd(A,B)
f2=A*B//f
print(f2)