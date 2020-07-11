import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()

cnt = [0] * (10**4+1)

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            tmp = ((i+j)**2 + (j+k)**2 + (k+i)**2) // 2
            if tmp < 10**4 + 1:
                cnt[tmp] += 1

for i in range(1, N+1):
    print(cnt[i])