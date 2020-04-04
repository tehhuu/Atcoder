#from queue import Queue #キューを使ったら1ケースだけTLEになった。
from collections import deque

H, W = map(int,input().split())
A = [list(input()) for i in range(H)]

dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

fin_d_max = 1

for s_i in range(H):
    for s_j in range(W):
        d_max = 0
        q_i = deque()
        q_j = deque()
        D = [[-1]*W for i in range(H)]
        flag = 1

        if A[s_i][s_j] == '.':
            D[s_i][s_j] = 0
            q_i.append(s_i)
            q_j.append(s_j)
            while len(q_i)!=0:
                i = q_i.popleft()
                j = q_j.popleft()
                for x in range(4):
                    ni = i+di[x]
                    nj = j+dj[x]
                    if ni<0 or ni>=H or nj<0 or nj>=W or A[ni][nj]== '#' or D[ni][nj]!=-1:
                        continue
                    else:
                        D[ni][nj] = D[i][j]+1
                        d_max = max(d_max, D[ni][nj])
                        q_i.append(ni)
                        q_j.append(nj)
        fin_d_max = max(fin_d_max, d_max)
                
print(fin_d_max)

'''
##4/4
import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
from collections import deque

H, W = mi()
S = [input() for i in range(H)]

d = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0
flag = dp2(0, W, H)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            flag = dp2(0, W, H)
            d.append([i, j, 0])
            flag[i][j] = 1
            while len(d)!=0:
                a = d.popleft()
                for k in range(4):
                    x, y = a[0]+dy[k], a[1]+dx[k]
                    if 0 <= x < H and 0 <= y < W:
                        if S[x][y] == '.' and flag[x][y] != 1:
                            d.append([x, y, a[2]+1])
                            flag[x][y] = 1
                            ans = max(ans, a[2]+1)

print(ans)
'''
                    
            
        