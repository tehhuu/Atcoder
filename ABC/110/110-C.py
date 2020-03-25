def ad_list_gen(S):
    l = len(S)
    ad_list = [[] for i in range(l)]
    al_dict = {}

    for i, moji in enumerate(S):
        if moji not in al_dict:
            al_dict[moji] = i
        else:
            ad_list[al_dict[moji]].append(i)
    
    return ad_list

S = input()
T = input()

ad_list = ad_list_gen(S)
ad_list2 = ad_list_gen(T)
print(ad_list)
if ad_list==ad_list2:
    print('Yes')
else:
    print('No')



            