N, K = map(int, input().split())

AB = [list(map(int, input().split())) for i in range(N)]

AB.sort(key=lambda x:x[0])
i = 0

while K-AB[i][1]>0:
    K -= AB[i][1]
    i += 1

print(AB[i][0])

'''
ab_list =[]
for i in range(N):
    for j in range(AB[i][1]):
        ab_list.append(AB[i][0])

print(ab_list[K+1])
'''

