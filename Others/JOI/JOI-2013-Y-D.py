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

## 2013 JOI 予選　D

N, D = mi()
l = [ii() for _ in range(N)]
t_to_c = [[] for _ in range(61)]
c_list = []

for i in range(D):
    a, b, c = mi()
    for j in range(a, b+1):
        t_to_c[j].append([i, c])
    c_list.append(c)

dp = dp2(0, D, N)

for num, c in t_to_c[l[0]]:
    dp[0][num] = -1

for i in range(N-1):
    for j in range(D):
        if dp[i][j] != 0:
            if dp[i][j] == -1:
                dp[i][j] = 0
            for num, c in t_to_c[l[i+1]]:
                dp[i+1][num] = max(dp[i][j] + abs(c - c_list[j]), dp[i+1][num])
                if dp[i+1][num] == 0:
                    dp[i+1][num] = -1

print(max(dp[N-1]))
