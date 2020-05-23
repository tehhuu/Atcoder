import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

S = input()
N = len(S)
A = [0]*(N+1)

i = 0
ind = 0
flag = 0
if S[0] == '>':
    while S[ind] == '>':
        ind += 1
        if ind >= N:
            flag = 1
            break
    num = ind
    for i in range(ind+1):
        A[i] = num
        num -= 1
i = ind

if flag:
    print(sum(A))
    exit()
if S.count('<') == N:
    print(N*(N+1)//2)
    exit()
if S == '><' or (len(S) == ind+1 and S[i-1:i+1] == '><'):
    print(2)
    exit()
while True:
    if S[i] == '<' and S[i+1] == '>':
        cnt = 0
        while True:
            cnt += 1
            if i+1+cnt > N-1 or S[i+1+cnt] == '<':
                break
        #print(i, cnt)
        if i+1-ind >= cnt+1:
            num = 1
            for j in range(ind+1, i+2):
                A[j] = num
                num += 1
            num = 0
            for j in reversed(range(i+2, i+cnt+2)):
                A[j] = num
                num += 1
        else:
            num = 1
            for j in range(ind+1, i+1):
                A[j] = num
                num += 1
            num = 0
            for j in reversed(range(i+1, i+cnt+2)):
                A[j] = num
                num += 1
        ind = i+cnt+1
        i += cnt
        #print(A)
    else:
        A[i+1] = A[i] + 1
    i += 1
    if i >= N-1:
        if i == N-1:
            A[i+1] = A[i] + 1
        break

#print(A)
print(sum(A))



