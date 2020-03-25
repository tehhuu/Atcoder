import sys

N, W = map(int, input().split())
WV = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
INF = 10**11+1
dp = [[INF]*(N+1) for j in range(N*(10**3)+10)]
i = 0
ans = INF
while(True):
        for j in range(1, N+1):
                w = WV[j-1][1]
                if i-w >= 0:
                        dp[i][j] = min(dp[i][j-1], dp[i-w][j-1]+WV[j-1][0])
                else:
                        dp[i][j] = min(dp[i][j-1], WV[j-1][0])
        if dp[i][N] > W and ans <= W:
                print(i)
                exit()
        ans = dp[i][N]
        i += 1