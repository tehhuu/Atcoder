N = int(input())
A = list(map(int, input().split()))

l = len(A)
f = [0] * l


f[0] = 0
flag=0
if A[0] == 1:
    flag = 1

for i in range(1, l):
    if A[0] == 1 and f[i-1]==0:
        if A[i] == i+1:
            f[i] = 0
        else:
            f[i] = 1
    elif f[i-1] != 0:
        if A[i] == i - f[i-1] + 1:
            f[i] = f[i-1]
        else:
            f[i] = f[i-1] + 1 
    else:
        if A[i] == 1:
            f[i] = i
        else:
            f[i] = 0

if f[l-1]==0 and flag==0:
    print(int(-1))
    exit(0)

print(f[l-1])
