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
import itertools #list(accumulate(A))

S = sys.stdin.readline().rstrip()
S_int = list(map(int, list(S)))
N = len(S)

if N==1:
    print(S)
    exit()

cnt = 0
for l in list(itertools.product([0, 1], repeat=N-1)):
    tmp = S_int[0]
    for i, kigo in enumerate(l):
        if kigo == 1:
            cnt += tmp
            tmp = S_int[i+1]
        else:
            tmp = tmp * 10 + S_int[i+1]
    cnt += tmp

print(cnt)
    



