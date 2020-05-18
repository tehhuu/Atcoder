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
    
N, M = mi()
rel = [[] for _ in range(N)]

mark = [-1]*N
mark[0] = 0
flag = [0]*N
flag[0] = 1
l = deque([0])

for i in range(M):
    s, t = mi()
    s -= 1
    t -= 1
    rel[s].append(t)
    rel[t].append(s)

flag[0] = 1
while l != deque([]):
    a = l.popleft()
    for num in rel[a]:
        if not flag[num]:
            mark[num] = a
            flag[num] = 1
            l.append(num)

if sum(flag) != N:
    print('No')
    exit()
print('Yes')
for i in range(1, N):
    print(mark[i]+1)


