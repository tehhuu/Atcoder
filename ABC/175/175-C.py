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

N, K, D = mi()
N = abs(N)

if K * D > N:
    num = N//D
    if not (num - K)%2:
        print(min(abs(N - D * (N//D)), abs(N - D * (N//D) - 2 * D)))
    else:
        print(min(abs(N - D * (N//D) + D), abs(N - D * (N//D) - D)))
else:
    print(N - D * K)
