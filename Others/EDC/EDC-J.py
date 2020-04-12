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
 
## メモ化再帰
## TLEコード

def rec(i, j, k):
    global dp
    if dp[i][j][k] != -1.0:
        return dp[i][j][k]
    if i+j+k == 0:
        return 0.0
 
    num = i+j+k
    ans = N_f
    if i > 0:
        ans += (rec(i-1, j, k) * i)
    if j > 0:
        ans += (rec(i+1, j-1, k) * j)
    if k > 0:
        ans += (rec(i, j+1, k-1) * k)
    ans /= num
    dp[i][j][k] = ans
    return ans
 
N = ii()
N_f = float(N)
A = li()
 
cnt = [0, 0, 0]
for a in A:
    cnt[a-1] += 1
 
dp = dp3(-1.0, cnt[2]+1, cnt[1]+cnt[2]+1, N+1)
dp[0][0][0] = 0
 
print(rec(cnt[0], cnt[1], cnt[2]))