import sys

N = int(input())

c = [list(map(int, sys.stdin.readline().split())) for i in range(N-1)]

for i in range(N-1):
    ans = c[i][0]+c[i][1]
    for j in range(i+1, N-1):
        if ans <= c[j][1]:
            ans = c[j][1] + c[j][0]
        elif ans % c[j][2] == 0:
            ans += c[j][0]
        else:
            ans = (ans//c[j][2]+1)*c[j][2] + c[j][0]
    print(ans)

print(0)