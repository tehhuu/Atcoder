N = int(input())

P = list(map(int, input().split()))

max_sum = 10**4+1
dp = [[0]*N for i in range(max_sum)]

dp[0][0]=dp[P[0]][0] = 1

for j in range(1, N):
    dp[0][j]=1
    for i in range(max_sum):
        if dp[i][j-1]==1:
            dp[i][j]=1
            dp[i+P[j]][j] = 1

print(sum([dp[i][N-1] for i in range(max_sum)]))
        
        