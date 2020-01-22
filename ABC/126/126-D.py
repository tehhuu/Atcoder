N, K = map(int, input().split())
sum_ratio = 0

for i in range(1, N+1):
        ten = i
        ratio = 1.0 / N
        while ten < K:
                ten *= 2
                ratio *= 0.5
        sum_ratio += ratio

print(sum_ratio)

