N, M = map(int, input().split())
#A = [int(input()) for i in range(M)]
flag = [True] *N

for i in range(M):
    flag[int(input())-1] = False
#A = [i*3 for i in range(N//3)]
#for i in range(N//3):
    #flag[i] = 1

mod = 10**9+7

dp = [0] * N

if flag[0]:
#if 1 not in A:
    dp[0] = 1
    if N>1:
        if flag[1]:
    #if (2 not in A) and N > 1:
            dp[1] = 2
elif N > 1:
    if flag[1]:
    #if 2 not in A:
        dp[1] = 1
    else:
        dp[1] = 0

loop = []
'''
for i in range(2, N):
    if i not in A:
        loop.append(i)
'''
for i in range(2, N):
    if flag[i]:
        dp[i] = (dp[i-2] + dp[i-1]) % mod
        #dp[i] = (sum(dp[i-2:i])) % mod

print(dp[N-1])
#print(dp)