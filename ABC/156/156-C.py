N = int(input())

X = sorted(list(map(int,input().split())))

ans = 10000000000

for i in range(X[0], X[N-1]+1):
        ans = min(ans, sum([(X[j]-i)**2 for j in range(N)]))

print(ans)


