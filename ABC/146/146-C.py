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

max_l = len(str(X))
for l in reversed(range(1, max_l+1)):
    if 10 ** (l-1) <= (X - B * l) // A:
        #print(min((X - B * l) // A, 10**9))
        if (X - B * l) // A < 10 ** l:
            print(min((X - B * l) // A, 10**9))
        else:
            print(min(10**l - 1, 10**9))
        break
else:
    print(0)
        
        

