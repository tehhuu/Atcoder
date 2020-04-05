import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

##moji利用したらTLE
S = input()
T = input()
ls = len(S)+1
lt = len(T)+1

dp = dp2(0, ls, lt)

#moji = [['']*ls for i in range(lt)]

for i in range(1, lt):
    for j in range(1, ls):
        if S[j-1]==T[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
            #moji[i][j] = moji[i-1][j-1] + S[j-1]
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                #moji[i][j] = moji[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                #moji[i][j] = moji[i][j-1]

#print(moji[lt-1][ls-1])
ans = ''
i = lt-1
j = ls-1
while i > 0 and j > 0:
    if dp[i][j] > dp[i-1][j-1] and S[j-1]==T[i-1]:
        ans += S[j-1]
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print(ans[::-1])

'''
##TLE

dp = [[[0, ''] for j in range(ls)] for i in range(lt)]

for i in range(1, lt):
    for j in range(1, ls):
        if S[j-1]==T[i-1]:
            dp[i][j][0] = dp[i-1][j-1][0]+1
            dp[i][j][1] = dp[i-1][j-1][1] + S[j-1]
        else:
            if dp[i-1][j][0] >= dp[i][j-1][0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]
#print(dp)
print(dp[lt-1][ls-1][1])
'''


        