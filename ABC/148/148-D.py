N = int(input())
A = list(map(int, input().split()))

cnt = 1
for a in A:
    if a==cnt:
        cnt+=1

if cnt==1:
    print(-1)
else:
    print(N-cnt+1)
