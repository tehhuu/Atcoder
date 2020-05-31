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
from decimal import Decimal

N = ii()
A = li()
ans = 1
for num in A:
    ans *= num
    if ans > 10**18:
        if 0 in A:
            print(0)
        else:
            print(-1)
        exit()

print(ans)


'''
N = ii()
A = li()
ans = 1
inf = Decimal('1000000000000000000')
for num in A:
    if ans <= inf / Decimal(str(num)):
        ans *= num
    else:
        if 0 in A:
            print(0)
        else:
            print(-1)
        exit()
print(ans)
'''

'''
N = ii()
A = li()
if 0 in A:
    print(0)
    exit()
ans = 1
for num in A:
    print(ans, 10**18 / num, 10**18//num)
    if ans < (10**18+1) / num or ans == 10**18//num:
        ans *= num
    else:
        print(-1)
        exit()
print(ans)
'''