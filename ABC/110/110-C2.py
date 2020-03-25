def norm_s(S):
    num = 97
    al_dict = {}
    new = ''
    for i, moji in enumerate(S):
        if moji not in al_dict:
            al_dict[moji] = i
            new += chr(num)
            num += 1
        else:
            new += new[al_dict[moji]]
    
    return new

S = input()
T = input()

new = norm_s(S)
new2 = norm_s(T)
if new==new2:
    print('Yes')
else:
    print('No')