N = int(input())
S = sorted([int(input()) for i in range(N)])

sum_s = sum(S)
if sum_s % 10 != 0:
        print(sum_s)
        exit()
else:
        for i in range(N):
                if S[i] % 10 != 0:
                        print(sum_s-S[i])
                        exit()

print(0)