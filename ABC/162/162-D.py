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

N = ii()
S = input()

c_r = c_g = c_b = 0
h = ''
for i, a in enumerate(S):
    if a == 'R':
        c_r += 1
        h += '1'
    if a == 'G':
        c_g += 1
        h += '2'
    if a == 'B':
        c_b += 1
        h += '7'

ans = c_r * c_g * c_b

for i in range(N):
    for j in range(i+1, N):
        if 2*j-i<N and int(h[i]) + int(h[j]) + int(h[2*j-i]) == 10:
            ans -= 1
print(ans)



            


