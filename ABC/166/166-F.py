import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

def cv(m):
    if m == 'A':
        return 0
    if m == 'B':
        return 1
    if m == 'C':
        return 2

def dfs(i, d, ans):
    if d[0]<0 or d[1]<0 or d[2]<0:
        return
    if i == N:
        print('Yes')
        for m in ans:
            print(m)
        exit()
    s, t = cv(S[i][0]), cv(S[i][1])
    d[s] += 1
    d[t] -= 1
    #print(i, D[s], D[t])
    ans[i] = S[i][0]
    dfs(i+1, D, ans)
    d[s] -= 2
    d[t] += 2
    #print(i, D[s], D[t])
    ans[i] = S[i][1]
    dfs(i+1, d, ans)
    d[s] += 1
    d[t] -= 1

N, *D = mi()
S = [sys.stdin.readline()[:2] for _ in range(N)]
ans = [0]*N
dfs(0, D, ans)
print('No')
    
'''
ans = []
sum_d = sum(D)
for i in range(N):
    s, t = cv(S[i][0]), cv(S[i][1])
    if D[s] == D[t] == 0:
            print('No')
            exit()
    if sum_d > 2:
        if D[s] >= D[t]:
            D[s] -= 1
            D[t] += 1
            ans.append(S[i][1])
        else:
            D[s] += 1
            D[t] -= 1
            ans.append(S[i][0])
    elif sum_d == 2:
        if D[s] == 2:
            D[s] -= 1
            D[t] += 1
            ans.append(S[i][1])
        elif D[t] == 2:
            D[t] -= 1
            D[s] += 1
            ans.append(S[i][0])
        elif D[s] == D[t] == 1:
            if i+1 < N:
                if S[i] == S[i+1]:
                    D[s] -= 1
                    D[t] += 1
                    ans.append(S[i][1])
                elif cv(S[i][0]) == s or cv(S[i][1]) == s:
                    D[s] += 1
                    D[t] -= 1
                    ans.append(S[i][0])
                else:
                    D[t] += 1
                    D[s] -= 1
                    ans.append(S[i][1])
            else:
                ans.append(S[i][0])
        else:
            D[s] = 1 - D[s]
            D[t] = 1 - D[t]
            if D[s] == 1:
                ans.append(S[i][0])
            else:
                ans.append(S[i][1])
    else:
        D[s] = 1 - D[s]
        D[t] = 1 - D[t]
        if D[s] == 1:
            ans.append(S[i][0])
        else:
            ans.append(S[i][1])

print('Yes')
for m in ans:
    print(m)
'''

            












    

