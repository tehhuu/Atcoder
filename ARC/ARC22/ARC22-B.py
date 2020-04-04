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
A = li()
right = 0
flag = [0]*(10**5+1)
ans = 0

for left in range(N):
    #flag[A[left]] = 1
    while right < N and flag[A[right]]!=1:
        flag[A[right]] = 1
        right += 1
    #print(left, right)
    ans = max(ans, right-left)
    if left == right:
        right += 1
    else:
        flag[A[left]] = 0

print(ans)
        
                    



