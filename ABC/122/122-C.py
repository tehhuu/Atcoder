import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
from itertools import accumulate #list(accumulate(A))

N, Q = mi()
S = input()
lr = li2(Q)

num = [0] * N

for i in range(N-1):
    if S[i:i+2] == 'AC':
        num[i] = 1

num = [0] + list(accumulate(num))

for s, t in lr:
    print(num[max(t-1, 0)]-num[max(s-1, 0)])
