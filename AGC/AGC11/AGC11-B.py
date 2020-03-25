N = int(input())
A = sorted(list(map(int, input().split())))

tmp = 0
sum_a = sum(A)
ind = N+1
for i in range(N-1):
    tmp += A[i]*2
    if tmp < A[i+1]:
        ind = i

if ind == N+1:
    print(N)
else:
    print(N-ind-1)



