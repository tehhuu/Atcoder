C = [list(map(int, input().split())) for i in range(3)]

for i in range(2):
    if C[i+1][0]-C[0][0] == C[i+1][1]-C[0][1] == C[i+1][2]-C[0][2]:
        continue
    else:
        print('No')
        exit()

for j in range(2):
    if C[0][j+1]-C[0][j] == C[1][j+1]-C[1][j] == C[2][j+1]-C[2][j]:
        continue
    else:
        print('No')
        exit()

print('Yes')







