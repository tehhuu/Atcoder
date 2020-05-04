S = {x:list(input()) for x in 'abc'}
print(S)
ban = 'a'
while S[ban]:
        S[ban].pop(0)
        print('a')

print(ban.upper())