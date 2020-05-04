import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

###BFS
from collections import deque

N, K = mi()
T = li2(N)

l = deque([0])

for i in range(N):
    for k in range(K**i):
        num = l.popleft()
        for j in range(K):
            l.append(num^T[i][j])

if 0 in l:
    print('Found')
else:
    print('Nothing')












