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
 
l = [i for i in range(1, N+1)]
 
if N % 2:
    for i in range(M):
        print(N//2-i, N//2+i+1)
else:
    for i in range(M//2, M):
        print(1+i-M//2, N-i+M//2)
    for i in range(M//2):
        print(N//2-i, N//2+i+2)
