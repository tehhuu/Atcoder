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
 
right = 1
cnt = 0

'''
mae = A[0]
for left in range(N):
    if left==right:
        right += 1
    mae = A[right-1]
    while right < N and A[right] > mae:
        mae = A[right]
        right += 1
    
    #print(left, right, mae)
    cnt += right-left
'''

for left in range(N):
    while right < N and A[right] > A[right-1]:
        right += 1
 
    cnt += right-left
    if left+1 == right:
        right += 1
 
print(cnt)
