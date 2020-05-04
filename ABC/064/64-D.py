import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
S = input()

pos = 0
r_cnt = 0

while pos < N and S[pos]==')':
    r_cnt += 1
    pos += 1

l_cnt = 0

for i in range(pos, N):
    if S[i]=='(':
        l_cnt += 1
    else:
        if l_cnt==0:
            r_cnt += 1
        else:
            l_cnt -= 1

print('('*r_cnt + S + ')'*l_cnt)
