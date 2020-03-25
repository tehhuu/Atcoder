from fractions import gcd
from functools import reduce

N, K = map(int, input().split())
A =list(map(int, input().split()))

if K <= max(A) and K % reduce(gcd, A) == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
