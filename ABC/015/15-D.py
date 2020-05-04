'''
W = int(input())

N, K = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]

dp = [[[0 for i3 in range(2)] for i2 in range(W+1)] for i1 in range(N+1)]


for i in range(1, N+1):
    for j in range(1, W+1):
        if j-A[i-1][0]>=0:
            if dp[i-1][j][1] < dp[i-1][j-A[i-1][0]][1] + A[i-1][1]:
                dp[i][j][0] = dp[i-1][j-A[i-1][0]][0] + 1
                dp[i][j][1] = dp[i-1][j-A[i-1][0]][1] + A[i-1][1]
            else:
                dp[i][j][0], dp[i][j][1] = dp[i-1][j][0], dp[i-1][j][1]
        elif dp[i][j-1][1] >= dp[i-1][j][1]:
            dp[i][j][0], dp[i][j][1] = dp[i][j-1][0], dp[i][j-1][1]
        else:
            dp[i][j][0], dp[i][j][1] = dp[i-1][j][0], dp[i-1][j][1]

for j in range(W, 1, -1):
    if dp[N][j][0] <= K:
        print(dp[N][j][1])
        exit()

print(0)
'''

W = int(input())
 
N, K = map(int, input().split())
 
A = [list(map(int, input().split())) for i in range(N)]
 
dp = [[[[], 0] for i2 in range(W+1)] for i1 in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, W+1):
        if j-A[i-1][0]>=0:
            if dp[i-1][j][1] < dp[i-1][j-A[i-1][0]][1] + A[i-1][1]:
                dp[i][j][0] = dp[i-1][j-A[i-1][0]][0][:]
                dp[i][j][0].append(A[i-1][1])
                dp[i][j][0] = sorted(dp[i][j][0], reverse=True)
                dp[i][j][1] = dp[i-1][j-A[i-1][0]][1] + A[i-1][1]
                if len(dp[i][j][0]) > K:
                    m = dp[i][j][0].pop(-1)
                    dp[i][j][1] -= m
            else:
                dp[i][j][0], dp[i][j][1] = dp[i-1][j][0][:], dp[i-1][j][1]
        elif dp[i][j-1][1] >= dp[i-1][j][1]:
            dp[i][j][0], dp[i][j][1] = dp[i][j-1][0][:], dp[i][j-1][1]
        else:
            dp[i][j][0], dp[i][j][1] = dp[i-1][j][0][:], dp[i-1][j][1]
 
print(dp[N][W][1])