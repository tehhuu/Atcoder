import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

## BFS

from collections import deque
N, M = mi()
memo = []
rel = [[] for i in range(N)]

for i in range(M):
    s, t = mi()
    s, t = s-1, t-1
    memo.append((s, t))
    rel[s].append(t)
    rel[t].append(s)

cnt = 0
que = deque()
for x in range(M):
    s, t = memo[x][0], memo[x][1]
    rel[s].remove(t)
    rel[t].remove(s)

    que.append(0)
    used = [0]*N
    while que != deque():
        v = que.popleft()
        for nv in rel[v]:
            if not used[nv]:
                used[nv] = 1
                que.append(nv)
    if sum(used) != N:
        cnt += 1

    rel[s].append(t)
    rel[t].append(s)

print(cnt)
                


        
        

