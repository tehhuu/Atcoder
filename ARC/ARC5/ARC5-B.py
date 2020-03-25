'''
import sys

x, y, W = input().split()

x = int(x)
y = int(y)

C = [sys.stdin.readline() for i in range(9)]

h_x = {'R':1, 'L':-1, 'U':0, 'D':0, 'RU':1, 'RD':1, 'LU':-1, 'LD':-1}
h_y = {'R':0, 'L':0, 'U':-1, 'D':1, 'RU':-1, 'RD':1, 'LU':-1, 'LD':1}

dx, dy = h_x[W], h_y[W]

ans = ''

for i in range(4):
    ans += C[y-1][x-1]
    if x+dx<1 or x+dx>9:
        dx *= (-1)
    if y+dy<1 or y+dy>9:
        dy *= (-1)
    x += dx
    y += dy

print(ans)
'''

x,y,w = input().split()
x, y = int(x)+7,int(y)+7
A = [input() for i in range(9)]
B = [a[1:][::-1] + a + a[:-1][::-1] for a in A]
C = B[1:][::-1] + B + B[:-1][::-1]
print(B)
print(C)