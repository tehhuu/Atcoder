S = input()
flag = 0

if len(S)%2 == 1:
    print('No')
    exit()
else:
    for i in range(len(S)//2):
        if S[i*2:i*2+2] != 'hi':
            flag = 1

if flag == 0:
    print('Yes')
else:
    print('No')