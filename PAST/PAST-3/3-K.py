import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N, Q = mi()
'''
to = [0 for i in range(N+1)]
head = [0 for i in range(N+1)]
table = [[i, i] for i in range(N+1)]

for _ in range(Q):
    f, t, x = mi()
    tmp = to[x]
    to[x] = table[t][1]
    head[table[t][1]] = x
    table[t][1] = table[f][1]
    table[f][1] = tmp
    if tmp == 0:
        table[f][0] = tmp 

print(table)
'''
table = [i for i in range(N+1)]
on_table = [i for i in range(N+1)]
to = [i for i in range(N+1)]

for _ in range(Q):
    #print(table)
    f, t, x = mi()
    if to[x] == x:
        table[f] = 0
    else:
        table[f] = to[x]

    if table[t] == 0:
        table[t] = x
        to[x] = x
    else:
        to[x] = table[t]

    on_table[x] = t

flag = [0]*(N+1)

def dfs(node):
    if flag[node]:
        return flag[node]
    if to[node] == node:
        flag[node] = node
        return node
    flag[node] = dfs(to[node])
    return flag[node]

for i in range(1, N+1):
    #print(flag)
    if not flag[i]:
        #print('a')
        print(on_table[dfs(i)])
    else:
        print(on_table[flag[i]])
        #print('b')

#print(flag)
#print(on_table)
#print(to)



