import sys

N , W = map(int, input().split())

WV = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

INF = (-1)*10**13

dp = [[0]*(1+W) for i in range(N+1)]
for j in range(1, W+1):
    dp[0][j] = INF
for i in range(1, N+1):
    for j in range(1, W+1):
        if j-WV[i-1][0]>=0 and dp[i-1][j-WV[i-1][0]]!=INF:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-WV[i-1][0]]+WV[i-1][1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][W])