N = int(input())
sum = N+1

for i in range(1, int(N**0.5//1)+1):
        if N % i == 0 and (i + (N // i) - 2 < sum):
                sum = i + (N // i) - 2

print(sum)