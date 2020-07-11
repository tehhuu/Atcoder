import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N, M = mi()
A = [10**5+1] + li()
XY = li2(M)

flag = [A[i] == i for i in range(N+1)]
rel = [[] for _ in range(N+1)]

for x, y in XY:
    if y in rel[x]:
        continue
    for num in rel[x]:
        if num not in rel[y]:
            rel[y].append(num)
            rel[num].append(y)
    for num in rel[y]:
        if num not in rel[x]:
            rel[x].append(num)
            rel[num].append(x)
    rel[x].append(y)
    rel[y].append(x)

print(flag)
print(rel)

for i in range(1, N):
    for j in rel[i]:
        if flag[i] or flag[j]:
            continue
        if A[j] == i or A[i] == j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            if A[i] == i:
                flag[i] = 1
            if A[j] == j:
                flag[j] = 1

print(flag)
print(sum(flag))

