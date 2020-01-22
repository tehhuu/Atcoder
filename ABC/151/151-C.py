N, M = map(int,input().split())
ps = [list(map(str,input().split())) for i in range(M)]

er_c = 0
ac_c = 0

if M == 0:
    print(0, 0)
    exit(0)

flag = [0]*N

for i in reversed(range(M)):
    if ps[i][1] == 'AC':
        flag[int(ps[i][0])-1] = 1

for i in range(M):
    if flag[int(ps[i][0])-1] == 1:
        if i == 0:
            if ps[i][1] == 'WA':
                er_c += 1
            else:
                ac_c += 1
                flag[int(ps[i][0])-1] = -1
        elif ps[i][1] == 'WA':
            er_c += 1
        elif ps[i][1] == 'AC':
                ac_c += 1
                flag[int(ps[i][0])-1] = -1

print(ac_c, er_c)
    


