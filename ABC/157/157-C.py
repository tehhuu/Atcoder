N, M = map(int,input().split())

S = [list(map(int,input().split())) for i in range(M)]

cnt = [0]*N
ans = 0

for i in range(M):
        if S[i][0]==1 and S[i][1]==0 and N!=1:
                print('-1')
                exit()
        if cnt[S[i][0]-1]!=0 and cnt[S[i][0]-1]!=S[i][1]:
                print('-1')
                exit()
        if N==1 and cnt[S[i][0]-1]!=S[i][1] and i > 0:
                print('-1')
                exit()
        else:
                cnt[S[i][0]-1] = S[i][1]

if N==1:
        print(cnt[0])
        exit()
if cnt[0]!=0:
        for i in range(N):
                ans += cnt[i] * (10**(N-1-i))
else:
        ans += 1 * (10**(N-1))
        for i in range(1, N):
                ans += cnt[i] * (10**(N-1-i))

print(ans)





