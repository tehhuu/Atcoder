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

N = ii()

h = [i for i in range(N)]
v = [i for i in range(N)]
rev = 0
#M = [[i*N + j for j in range(N)] for i in range(N)]

Q = ii()

for _ in range(Q):
    req = li()
    if (req[0]==1 and rev==0) or (req[0]==2 and rev==1):
        h[req[1]-1], h[req[2]-1] = h[req[2]-1], h[req[1]-1]

    elif (req[0]==2 and rev==0) or (req[0]==1 and rev==1):
        v[req[1]-1], v[req[2]-1] = v[req[2]-1], v[req[1]-1]

    elif req[0] == 3:
        rev = 1-rev
    else:
        if rev:
            print(h[req[2]-1] * N + v[req[1]-1])
        else:
            print(h[req[1]-1] * N + v[req[2]-1])