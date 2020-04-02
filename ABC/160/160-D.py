import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]

N, X, Y = mi()

dp = [0]*(N)

for i in range(1, N):
    for j in range(i+1, N+1):
        dp[min(j-i, abs(i-X)+1+abs(Y-j))] += 1

for i in range(1, N):
    print(dp[i])
