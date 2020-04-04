'''
###2/16
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
'''

###4/3
import sys
def ii(): return int(sys.stdin.readline())
from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
S = [input() for i in range(N)]
d = defaultdict(int)

for word in S:
    d[word] += 1

d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)

num = d2[0][1]
ans = []

for i in range(len(d2)):
    if num != d2[i][1]:
        break
    ans.append(d2[i][0])

for word in sorted(ans):
    print(word)