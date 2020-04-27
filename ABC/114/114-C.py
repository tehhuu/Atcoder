import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
import itertools #list(accumulate(A))
from collections import deque

N = ii()
que = deque([33, 35, 37, 53, 55, 57, 73, 75, 77])
ele = '357'

ind = 0
while True:
    num = que[ind] * 10
    que.append(num + 3)
    que.append(num + 5)
    que.append(num + 7)
    if len(str(num)) >= 10:
        break
    ind += 1

ind = bisect.bisect_right(que, N)

cnt = 0
for i in range(ind):
    tmp = str(que[i])
    for e in ele:
        if e not in tmp:
            cnt += 1
            break

print(ind - cnt)






