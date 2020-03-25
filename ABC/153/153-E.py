H, N = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

INF = 10**10+1

dp = [[INF]*(H+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    dp[i][0] = 0
    A = AB[i-1][0]
    for j in range(1, H+1):
        if j-AB[i-1][0]>=0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-AB[i-1][0]]+AB[i-1][1])
        else:
            dp[i][j] = min(dp[i-1][j], AB[i-1][1])

print(dp[N][H])


        