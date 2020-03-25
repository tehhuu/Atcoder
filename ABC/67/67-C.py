N = int(input())
A = list(map(int, input().split()))

sum_a = sum(A)
x = 0
ans = 1000000000000000

for i in range(N-1):
        x += A[i]
        ans = min(ans, abs(2*x-sum_a))

print(ans)