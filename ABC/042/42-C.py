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
#from itertools import accumulate #list(accumulate(A))

## BFSで順番に列挙

from collections import deque

N, K = mi()
D = li()
r = [i for i in range(10) if i not in D]

if r[0]==0:
    que = deque(r[1:])
else:
    que = deque(r)

# Nが一桁以下の場合
for num in que:
    if N <= num:
        print(num)
        exit()

## BFSで順に列挙。N以上の数が出現したら出力して終了。
i = 0
while True:
    base = que[i]*10
    for num in r:
        new = base + num
        if new >= N:
            print(new)
            exit()
        que.append(new)
    i += 1
