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

from collections import deque

N, X, Y = mi()
X, Y = X+205, Y+205
H, W = 410, 410
S = [['.']*W for _ in range(H)]

for _ in range(N):
    x, y = mi()
    S[x+205][y+205] = '#'

d = dp2(-1, W, H)
d[205][205] = 0 #適宜変更
que = deque([[205, 205]])

h = [1, 0, -1, 0, 1, -1]
v = [0, -1, 0, 1, 1, 1]

while que != deque():
    i, j = que.popleft()
    for x in range(6):
        di, dj = h[x], v[x]
        if 0 <= i+di < H and 0 <= j+dj < W:
            if S[i+di][j+dj] !='#' and d[i+di][j+dj] == -1:
                d[i+di][j+dj] = d[i][j] + 1
                if i+di == X and j+dj == Y:
                    print(d[X][Y])
                    exit()
                que.append([i+di, j+dj])

print(-1)
