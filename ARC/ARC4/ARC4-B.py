import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
D = sorted([ii() for i in range(N)])

sum_d = sum(D)
print(sum_d)
if N==1:
    print(D[0])
elif N==2:
    print(D[1]-D[0])
else:
    for hen in D:
        h_sum_d = float(sum_d) / 2
        if h_sum_d <= hen:
            print(sum_d - 2*(sum_d - D[N-1]))
            exit()
    print(0)


