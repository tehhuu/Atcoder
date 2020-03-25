N, K = map(int, input().split())
H = list(map(int, input().split()))

INF = 10**9

dp = [INF]*N
dp[0] = 0

for i in range(N):
    for j in range(1, min(i+1, K+1)):
        dp[i] = min(dp[i], dp[i-j]+abs(H[i]-H[i-j]))

print(dp[N-1])