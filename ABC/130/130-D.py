import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N, x = mi()
A = li()
ans = 0
wa = 0
right = 0

for left in range(N):
    while right < N:
        if wa+A[right] >= x:
            ans += N-right
            break
        
        wa += A[right]
        right += 1
    
    if left == right:
        right += 1
    else:
        wa -= A[left]

print(ans)