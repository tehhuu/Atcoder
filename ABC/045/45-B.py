S = [input() for i in range(3)]

def abctoint(x):
        if x=='a':
                return 0
        elif x=='b':
                return 1
        else:
                return 2

ban = 0

while True:
        if len(S[ban]) == 0:
                break
        next_ban = abctoint(S[ban][0])
        S[ban] = S[ban][1:]
        ban = next_ban

if ban == 0:
        print('A')
elif ban == 1:
        print('B')
else:
        print('C')

        