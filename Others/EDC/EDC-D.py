import sys

N, W = map(int, input().split())
WV = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
'''
w = [0]*N
v = [0]*N
for i in range(N):
        w[i], v[i] = map(int, sys.stdin.readline().split())
'''
dp = [[0]*(N+1) for j in range(W+1)]

for i in range(1, W+1):
        for j in range(1, N+1):
                if i - w[j-1]>=0:
                #if i - WV[j-1][0]>=0:
                        dp[i][j] = max(dp[i-w[j-1]][j-1]+v[j-1], dp[i][j-1])
                        #dp[i][j] = max(dp[i-WV[j-1][0]][j-1]+WV[j-1][1], dp[i][j-1])
                else:
                        dp[i][j] = dp[i][j-1]

print(dp[W][N])

'''

dp = [0]*(W+1)

for i in range(1, W+1):
        for j in range(N):
                if i - WV[j][0]>=0:
                        dp[i] = max(dp[i-WV[j][0]]+WV[j][1], dp[i])
                        if i==W:
                                print(i, j)
                                print(dp)
        print(dp)

print(dp[W])

'''