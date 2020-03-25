A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
B = [int(input()) for i in range (N)]

cnt = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for b in B:
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                cnt[i][j] = 1

for i in range(3):
    if sum([cnt[j][i] for j in range(3)]) == 3:
        print('Yes')
        exit()
    if sum([cnt[i][j] for j in range(3)]) == 3:
        print('Yes')
        exit()
if cnt[0][0]+cnt[1][1]+cnt[2][2]==3:
    print('Yes')
    exit()
if cnt[0][2]+cnt[1][1]+cnt[2][0]==3:
    print('Yes')
    exit()

print('No')

    





                        