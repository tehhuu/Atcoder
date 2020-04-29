import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

H, W = mi()
S = [input() for _ in range(H)]

org = [['#'] * W for _ in range(H)]

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, 1, 1, 0, -1, -1, -1, 0, 1]

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            for k in range(9):
                y, x = i+di[k], j+dj[k]
                if 0<= y < H and 0<= x < W:
                    org[y][x] = '.'

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            for k in range(9):
                y, x = i+di[k], j+dj[k]
                if 0<= y < H and 0<= x < W:
                    if org[y][x] == '#':
                        break
            else:
                print('impossible')
                exit()
print('possible')
for i in range(H):
    for j in range(W):
        print(org[i][j], end='')
    print('')
            



