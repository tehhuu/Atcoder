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

## itertoolsを使った準753数の列挙

import itertools

N = ii()
l = []

for keta in range(3, 10):
    for koho in itertools.product(['3', '5', '7'], repeat=keta):
        l.append(int(''.join(koho)))
l.sort()

ele = '357'
cnt = 0
for num in l:
    if num > N:
        break
    num = str(num)
    if all(e in num for e in ele):
        cnt += 1

print(cnt)













