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
from collections import deque

## DFS

N, M, Q = mi()
abcd = li2(Q)

def dfs(num, length):
    if length == N:
        l.append(num)
        return
    last = int(num[-1])
    for i in range(last, M):
        dfs(num + str(i), length+1)

l = []
dfs('0', 1)

ans = 0
for num in l:
    cnt = 0
    num = list(map(int, list(num)))
    for i in range(Q):
        if num[abcd[i][1]-1] - num[abcd[i][0]-1] == abcd[i][2]:
            cnt += abcd[i][3]
    ans = max(ans, cnt)

print(ans)