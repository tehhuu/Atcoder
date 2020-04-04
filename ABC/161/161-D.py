import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

K = ii()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(K-9):
    a = l[i]
    b = int(str(a)[-1])
    if b!=0 and b != 9:
        for k in range(b-1, b+2):
            l.append(int(str(a)+str(k)))
    elif b==0:
        for k in range(b, b+2):
            l.append(int(str(a)+str(k)))
    else:
        for k in range(8, 10):
            l.append(int(str(a)+str(k)))

print(l[K-1])


