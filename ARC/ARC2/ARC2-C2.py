import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
S = input()
l = []
abxy = 'ABXY'
ans = N

#二文字の組み合わせの全パターンをリストに格納
for i in range(4):
    for j in range(4):
        l.append(abxy[i]+abxy[j])

for i in range(16):
    for j in range(i+1, 16):
        dp = [num for num in range(N+1)]

        for k in range(N-1):
            #x = k + 1
            if S[k:k+2] == l[i] or S[k:k+2] == l[j]:
                dp[k+1] = min(dp[k]+1, dp[k+1])
                dp[k+2] = min(dp[k]+1, dp[k+2])
            else:
                dp[k+2] = min(dp[k+1]+1, dp[k+2])

        ans = min(ans, dp[N])

print(ans)





