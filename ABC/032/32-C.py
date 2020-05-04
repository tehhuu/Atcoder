import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N, K = mi()
S = [ii() for i in range(N)]

seki = 1
right = 0
ans = 0

if 0 in S:
    print(N)
    exit()

for left in range(N):
    while right < N:
        if seki*S[right] > K:
            break
        seki *= S[right]
        right += 1
    ans = max(ans, right-left)
    if left==right:
        right += 1
    else:
        seki //= S[left]

print(ans)
