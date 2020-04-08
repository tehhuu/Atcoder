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

n, d, k = mi()
lr = li2(d)
st = li2(k)

for s, t in st:
    start = end = 0
    flag = 0
    for j in range(d):
        l, r = lr[j][0], lr[j][1]
        if flag == 0 and l <= s <= r:
            flag = 1
            start = l
            end = r
        if flag:
            if end >= l and r >= start:
                start = min(start, l)
                end = max(end, r)
            if start <= t <= end:
                print(j+1)
                break
