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

N = ii()

A = [input() for _ in range(N)]
ans = ''

for i in range(N//2):
    head = set(A[i])
    tail = set(A[N-1-i])
    for moji in head:
        if moji in tail:
            ans += moji
            break
    else:
        print(-1)
        exit()

if N%2:
    print(ans + A[N//2][0] + ans[::-1])
else:
    print(ans + ans[::-1])


