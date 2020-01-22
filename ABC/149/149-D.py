N, K = map(int,input().split())
z_list = list(map(int,input().split()))
T = str(input())
sum = 0
aiko_flag=[0] * K

for i in range(N):
    if i > K-1:
        if T[i] == 'r' and (T[i-K] != 'r' or aiko_flag[(i-K) % K] == 1):
            sum = sum + z_list[2]
            aiko_flag[i % K] = 0
        elif T[i] == 's'and (T[i-K] != 's' or aiko_flag[(i-K) % K] == 1):
            sum = sum + z_list[0]
            aiko_flag[i % K] = 0
        elif T[i] == 'p' and (T[i-K] != 'p' or aiko_flag[(i-K) % K] == 1):
            sum = sum + z_list[1]
            aiko_flag[i % K] = 0
        else:
            aiko_flag[i % K] = 1
    elif i < K:
        if T[i] == 'r':
            sum = sum + z_list[2]
        elif T[i] == 's':
            sum = sum + z_list[0]
        elif T[i] == 'p':
            sum = sum + z_list[1]

print(sum)


