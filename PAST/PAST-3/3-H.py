import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N, L = mi()
X = li()

h_flag = [0]*L
for hardle in X:
    h_flag[hardle] = 1

t1, t2, t3 = mi()

dp = [float('inf')]*(L+5)
dp[0] = 0

for i in range(L):
    if i+2 <= L:
        dp[i+2] = min(dp[i+2], dp[i] + t1 + t2 + h_flag[i]*t3)
    else:
        dp[L] = min(dp[L], dp[i] + t1*0.5 + t2*(L-i-0.5) + h_flag[i]*t3)

    if i+4 <= L:
        dp[i+4] = min(dp[i+4], dp[i] + t1 + t2*3 + h_flag[i]*t3)
    else:
        dp[L] = min(dp[L], dp[i] + t1*0.5 + t2*(L-i-0.5) + h_flag[i]*t3) 

    dp[i+1] = min(dp[i+1], dp[i] + t1 + h_flag[i]*t3)

#print(dp)
print(int(dp[L]))