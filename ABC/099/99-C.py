N = int(input())

roku = kyu = 1
h_list = [1]

while(roku<N):
    roku *= 6
    h_list.append(roku)

while(kyu<N):
    kyu *= 9
    h_list.append(kyu)

#print(h_list)

FIN = 10**7
dp = [FIN]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(len(h_list)):
        if h_list[j] <= i:
            dp[i] = min(dp[i], dp[i-h_list[j]]+1)
            #print(dp)

print(dp[N])
        


