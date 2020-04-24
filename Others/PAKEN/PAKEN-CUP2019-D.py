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

## パ研合宿2019 第3日「パ研杯2019」 D問題

N = ii()
S = [input() for _ in range(5)]

color = ['R', 'W', 'B']
dp = dp2(0, 3, 2)

def paint(ind, c):
    return 5 - sum([S[i][ind] == color[c] for i in range(5)])

for s in range(3):
    dp[0][s] = 5 - sum([S[i][0] == color[s] for i in range(5)])

for x in range(1, N):
    for j in range(3):
        i = x%2
        pi = 1 - i
        k, l = (j+1)%3, (j+2)%3
        dp[i][j] = min(dp[pi][k]+paint(x, j), dp[pi][l]+paint(x, j))

ans = min(dp[(N-1)%2])
print(ans)

