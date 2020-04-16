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

from collections import deque

H, W = mi()
sx, sy = mi()
gx, gy = mi()
sx, sy , gx, gy = sx-1, sy-1, gx-1, gy-1
M = [input() for _ in range(H)]

que = deque([[sx, sy]])
d = dp2(-1, W, H)
d[sx][sy] = 0
y = [1, 0, -1, 0]
x = [0, -1, 0, 1]

while que!=deque():
    [vx, vy] = que.popleft()
    for i in range(4):
        dx, dy = x[i], y[i]
        if 0<= vx+dx < H and 0<= vy+dy < W:
            if M[vx+dx][vy+dy] != '#' and d[vx+dx][vy+dy]==-1:
                d[vx+dx][vy+dy] = d[vx][vy] + 1
                que.append([vx+dx, vy+dy])

print(d[gx][gy])





