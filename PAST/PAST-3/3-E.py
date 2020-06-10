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

N, M, Q = mi()

rel = [[] for _ in range(N)]

for _ in range(M):
    s, t = mi()
    rel[s-1].append(t-1)
    rel[t-1].append(s-1)
color = li()

for _ in range(Q):
    req = li()
    print(color[req[1]-1])
    if req[0] == 1:
        for node in rel[req[1]-1]:
            color[node] = color[req[1]-1]
    else:
        color[req[1]-1] = req[2]


