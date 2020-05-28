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

N, K, S = mi()
A = [0]*N

if N == 1:
    print(S)
    exit()
if K==N:
    for i in range(N):
        print(S, end="")
        if i != N-1:
            print(' ', end="")
    exit()
if S == 1:
    for i in range(K):
        print(1, end="")
        if i != N-1:
            print(' ', end="")
    for i in range(K, N):
        print(2, end="")
        if i != N-1:
            print(' ', end="")
    exit()

mod = 10**9
if not S % 2:
    for i in range(K+1):
        A[i] = S//2
    for i in range(K+1, N):
            A[i] = (S + 1) % mod + 1
else:
    for i in range(K+1):
        if i % 2:
            A[i] = S//2
        else:
            A[i] = S//2 + 1
    for i in range(K+1, N):
        A[i] = (S + 1) % mod + 1

for i, num in enumerate(A):
    print(num, end="")
    if i != N-1:
        print(' ', end="")