import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def dfs(n, value):
    if n == N:
        if value==0:
            global flag
            flag = True
    else:
        for i in range(K):
            dfs(n+1, value^T[n][i])

def dfs2(n, value):
    if n == N:
        if value==0:
            #global flag
            #flag = True
            return True
        else:
            return False
    else:
        for i in range(K):
            if(dfs2(n+1, value^T[n][i])):
                return True
        return False

N, K = mi()
T = li2(N)
flag = False

#dfs(0, 0)
flag = dfs2(0, 0)

if flag == True:
    print('Found')
else:
    print('Nothing')













