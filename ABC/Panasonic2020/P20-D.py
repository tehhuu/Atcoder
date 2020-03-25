from collections import deque

N = int(input())

l = deque(['a'])

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in range(1, N):
    len_l = len(l)
    for k in range(len_l):
        x = l.popleft()
        for j in range(len(set(x))+1):
            l.append(x+alpha[j])

for i in l:
    print(i)
        