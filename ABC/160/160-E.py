import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]

X, Y, A, B, C = mi()
P = sorted(li())[-X:]
Q = sorted(li())[-Y:]
r = sorted(li())

p = sorted(P+Q)

#len_r = len(r)-1
a_p = p.pop(-1)
a_r = r.pop(-1)
cnt = 0

for i in range(X+Y):
    if a_p >= a_r:
        cnt += a_p
        if p!=[]:
            a_p = p.pop(-1)
        else:
            break
    else:
        cnt += a_r
        if r==[]:
            a_r = 0
        else:
            a_r = r.pop(-1)
        
print(cnt)


