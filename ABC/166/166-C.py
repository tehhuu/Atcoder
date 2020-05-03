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

N, M = mi()
A = li()

flag = [0]*N
# 同じ高さの山を記録
flag2 = [0]*N

for i in range(M):
    a, b = mi()
    a -= 1
    b -= 1
    flag[a] = max(A[a], A[b], flag[a])
    flag[b] = max(A[a], A[b], flag[b])
    if A[a] == A[b]:
        flag2[a] = flag2[b] = 1
cnt = 0
for i in range(N):
    if A[i] >= flag[i] and not flag2[i]:
        cnt += 1
print(cnt)
