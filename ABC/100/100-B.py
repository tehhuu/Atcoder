D, N = map(int,input().split())

n = 1

for i in range(1, D+1):
        n *= 100
if N == 100:
        N = 101
print(n * N)