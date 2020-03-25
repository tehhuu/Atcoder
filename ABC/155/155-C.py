N = int(input())

A = [input() for i in range(N)]

dic = {}

for i in A:
        if i not in dic:
                dic[i] = 1
        else:
                dic[i] += 1

de = 0

ans_list = []
#dic2 =　sorted(dic.values(), reverse=True)

for k, v in sorted(dic.items(), key=lambda x: x[1], reverse = True):
        if v != de and de !=0:
                break
        else:
                ans_list.append(k)
        de = v

ans_list_n = sorted(ans_list)


for i in ans_list_n:
        print(i)