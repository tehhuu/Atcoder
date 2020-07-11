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

H, W, K = mi()
C = [input() for i in range(H)]

B_i = 2 ** H
B_j = 2 ** W

ans = 0
for x in range(B_i):
    for y in range(B_j):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if (x & (1 << i)) or y & (1 << j):
                    continue
                if C[i][j] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
                
print(ans)
