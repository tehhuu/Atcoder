import sys

N = int(input())

A = [int(sys.stdin.readline()) for i in range(N)]

flag = [0]*(10**5+1)
cnt = 0

for i in A:
    if flag[i]==0:
        flag[i] = 1
    else:
        cnt += 1

print(cnt)