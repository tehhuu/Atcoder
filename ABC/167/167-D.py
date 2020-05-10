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

N, K = mi()
A = li()
flag = [0]*N
l = []
i = 1
ind = 0
while True:
    flag[ind] = i
    l.append(ind+1)
    if not flag[A[ind]-1]:
        ind = A[ind]-1
    else:
        ind = A[ind]-1
        break
    i += 1

if K <= flag[ind] - 1:
    print(l[K])
    exit()

if ind != 0:
    K -= flag[ind] -1
    i -= flag[ind] -1
    l = l[flag[ind] -1:]
    
print(l[K%i])
