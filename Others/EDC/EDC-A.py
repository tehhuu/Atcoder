N = int(input())
H = list(map(int, input().split()))

INF = 10**10
dp = [INF]*N
dp[0] = 0
dp[1] = abs(H[1]-H[0])
for i in range(2, N):
    dp[i] =  min(dp[i-2]+abs(H[i]-H[i-2]), dp[i-1]+abs(H[i]-H[i-1]))

print(dp[N-1])


