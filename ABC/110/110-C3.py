S = input()
T = input()

def normalized(S):
    m_set = list()
    for moji in S:
        if moji not in m_set:
            m_set.append(moji)
    m_dic = {m : i for i, m in enumerate(m_set)}
    ad_list = [m_dic[moji] for moji in S]

    return ad_list

print('Yes' if normalized(S)==normalized(T) else 'No')