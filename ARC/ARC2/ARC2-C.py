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
l = []
abxy = 'ABXY'
ans = N
cnt = 0
for i in range(4):
    for j in range(4):
        l.append(abxy[i]+abxy[j])
#print(l)
for i in range(16):
    for j in range(i+1, 16):
        x = 0
        while x < N:
            if x!=N-1 and (S[x:x+2] == l[i] or S[x:x+2] == l[j]):
                cnt += 1
                x += 2
            else:
                cnt += 1
                x += 1
        
        ans = min(ans, cnt)
        cnt = 0

print(ans)
            
        





