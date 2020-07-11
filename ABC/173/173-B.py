import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()

L = [input() for i in range(N)]

#cnt = Counter(L).most_common()
cnt = defaultdict(int)
cnt['AC'] = 0
cnt['WA'] = 0
cnt['TLE'] = 0
cnt['TLE'] = 0
for s in L:
    cnt[s] += 1

print('AC x', cnt['AC'])
print('WA x', cnt['WA'])
print('TLE x', cnt['TLE'])
print('RE x', cnt['RE'])