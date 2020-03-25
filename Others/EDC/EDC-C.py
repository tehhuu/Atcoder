import sys

N = int(input())

dp = [[0]*3  for i in range(N)]

dp[0][0], dp[0][1], dp[0][2] = map(int, sys.stdin.readline().split())

tmp = [0, 0, 0]

for i in range(1, N):
    tmp[0], tmp[1], tmp[2] = map(int, sys.stdin.readline().split())
    for j in range(3):
        dp[i][j] = max(dp[i-1][(j+1)%3]+tmp[j], dp[i-1][(j+2)%3]+tmp[j])

print(max(dp[N-1]))