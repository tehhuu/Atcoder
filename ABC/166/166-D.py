import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

X = ii()
'''
lim = 10**3

for a in range((-1)*lim, lim+1):
    for b in range((-1)*lim, lim+1):
        if a**5 - b**5 == X:
            print(a, b)
            exit()
'''
i = 0
while True:
    for j in range((-1)*i, i):
        if i**5 - j**5 == X:
            print(i, j)
            exit()
    i += 1
    