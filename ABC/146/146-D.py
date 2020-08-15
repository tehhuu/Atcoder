import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
'''
N = ii()
num = [0] * N
ST = li2(N-1)

for s, t in ST:
    num[s-1] += 1
    num[t-1] += 1

max_k = max(num)
print(max_k)

cnt = [1] * N
#for i in range(N):
    #count[i] = num[i]

rel = [[] for _ in range(N)]

for s, t in ST:
    for k in range(1, max(num[s-1], num[t-1])+1):
        if (k not in rel[s-1]) and (k not in rel[t-1]):
            print(k)
            break
    rel[s-1].append(k)
    rel[t-1].append(k)
'''
from collections import deque

N = ii()
d = defaultdict(int)
ST = li2(N-1)
rel = [[] for _ in range(N)]
q = deque()

for s, t in ST:
    d[(s-1, t-1)] = -1
    rel[s-1].append(t-1)
    rel[t-1].append(s-1)

ind = (0, 0)

for i in range(N):
    if len(rel[i]) > ind[1]:
        ind = (i, len(rel[i]))

s = ind[0]
max_k = ind[1]
c = 1
for t in rel[s]:
    d[(min(s, t), max(s, t))] = c
    q.append((c, t))
    c += 1

while q != deque():
    cs = q.popleft()
    c, s = cs[0], cs[1]
    counter = 1
    for t in rel[s]:
        if d[(min(s, t), max(s, t))] == -1:
            color = (c + counter) % max_k
            d[(s, t)] = color
            counter += 1
            q.append((color, t))

print(ind[1])
for s, t in ST:
    if (d[(s-1, t-1)] + 1) % max_k == 0:
        print(max_k)
    else:
        print((d[(s-1, t-1)] + 1) % max_k)