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

N = ii()
x = []
for i in range(N):
    tmp = ii()
    x.append(li2(tmp))

if N == 1:
    if x != [[[1, 0]]]:
        print(1)
        exit()
    else:
        print(0)
        exit()

B = 2 ** N
ans = 0
no = [0] * N
rel = []

def dfs(i):
    global visited
    global table
    visited[i] = 1
    for a, b in x[i]:
        if table[a-1] != -1 and table[a-1] != b:
            global flag_ok
            flag_ok = 1
            break
        table[a-1] = b
        if b == 1 and not visited[a-1]:
            dfs(a-1)

for i in range(N):
    visited = [0] * N
    table = [-1] * N
    flag_ok = 0

    dfs(i)

    if not flag_ok:
        rel.append(table)
    else:
        rel.append([0] * N)
        no[i] = 1

print(no)
print(rel)

for i in range(B):
    sin = [-1] * N
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            if no[j]:
                break
            cnt += 1
            for k in range(N):
                if sin[k] != -1 and rel[j][k] != sin[k]:
                    break
                sin[k] = rel[j][k]
            else:
                continue
            break
    else:
        ans = max(ans, cnt)

print(ans)