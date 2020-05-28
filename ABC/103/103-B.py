
S = input()
T = input()

N = len(S)

for i in range(N):
    if S[N-i:] + S[:N-i] == T:
        print('Yes')
        exit()
print('No')