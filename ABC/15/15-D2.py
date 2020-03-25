import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
 
def solve(K, W, N, A):
    dp = dp3(0, W+1, N+1, K+1)
    for z in range(1, K+1):
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j-A[i-1][0]>=0:
                    dp[z][i][j] = max(dp[z-1][i-1][j-A[i-1][0]]+A[i-1][1], dp[z][i-1][j])
                else:
                    dp[z][i][j] = dp[z][i-1][j]
                
    print(dp[K][N][W])
 
if __name__ == '__main__':
    W = ii()
    N, K = li()
    A = li2(N)
    solve(K, W, N, A)