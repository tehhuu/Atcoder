import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

## floatは16桁までしか保証しない
## B*100がダメなのは 2.51*100 = 250.99999999999997 のようになる場合があるから
from decimal import Decimal

A, B = map(str, sys.stdin.readline().split())
A = Decimal(A)
B = Decimal(B)
print(A * B//1)


'''
四捨五入で誤差の影響をなくす
A, B = map(str, sys.stdin.readline().split())
A = int(A)
B = int(round(float(B)*100))
print(A*B//100)
'''

'''
#微小な数を足してあげることで誤差の影響をなくす
A, B = map(str, sys.stdin.readline().split())
A = int(A)
B = int(float(B)*100+0.1)
print(A*B//100)
'''

'''
#そもそもfloatを経由しなければいい
A, B = map(str, sys.stdin.readline().split())
A = int(A)
if B[0] == '0':
    B = int(B[2:])
else:
    B = int(B.replace('.', ''))
print(A*B//100)
'''