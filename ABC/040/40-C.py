import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
 
N = ii()
A = li()
 
dp = [0]*(N+1)
 
dp[1] = 0
dp[2] = abs(A[1]-A[0])
 
for i in range(3, N+1):
    dp[i] = min(abs(A[i-1]-A[i-2])+dp[i-1], abs(A[i-1]-A[i-3])+dp[i-2])
 
print(dp[N])
