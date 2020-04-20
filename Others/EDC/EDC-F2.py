import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

S = input()
T = input()

ls, lt = len(S), len(T)
dp = dp2(0, ls+1, lt+1)

# 配るDP
for i in range(lt):
    for j in range(ls):
        dp[i][j+1] = max(dp[i][j], dp[i][j+1])
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if S[j] == T[i]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

'''
# 貰うDP
for i in range(1, lt+1):
    for j in range(1, ls+1):
        if S[j-1] == T[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
'''


i, j = lt, ls
ans = ''

# 復元
while dp[i][j] != 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans += S[j-1]
        i -= 1
        j -= 1

print(ans[::-1])
