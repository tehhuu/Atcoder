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

A, B, X = mi()

end = X
start = 0

while True:
    mid = (start + end) // 2
    if A * mid + B * len(str(mid)) > X:
        end = mid
    else:
        start = mid
    if (start + end) // 2 == mid:
        print(min(mid, 10**9))
        exit()
        
        

