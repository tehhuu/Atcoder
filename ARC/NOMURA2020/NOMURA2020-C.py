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

N = ii()
A = li()

if N == 0:
    if A == [1]:
        print(1)
    else:
        print(-1)
    exit()

max_a = [0]*(N+1)
max_a[0] = 1 - A[0]

for i in range(1, N+1):
    max_a[i] = max_a[i-1] * 2 - A[i]
    if max_a[i] < 0:
        print(-1)
        exit()

cnt_list = [0]*(N)
cnt_list[-1] = min(A[-1], max_a[N-1])

for i in reversed(range(N-1)):
    if cnt_list[i+1] + A[i+1] <= max_a[i]:
        cnt_list[i] = cnt_list[i+1] + A[i+1]
    else:
        cnt_list[i] = max_a[i]

ans = sum(cnt_list) + sum(A)

print(ans)