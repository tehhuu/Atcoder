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
 
## 2015 JOI 本戦　B

def main():
    N = ii()
    A = tuple([ii() for _ in range(N)])
    #A = [ii() for _ in range(N)]

    dp = dp2(0, N, N)
    ## メモ化再帰
    def rec(i, j):
        if dp[i][j]:
            return dp[i][j]
        if j==i:
            dp[i][j] = A[i]
            return A[i]
        if j-i==1 or j-i==(-1)*(N-1):
            dp[i][j] = max(A[j], A[i])
            return dp[i][j]
        # JOI が A[i] を選んだ場合
        # IOI は A[j] と A[(i+1)%N] のうち大きい方を取る
        if A[j] > A[(i+1)%N]:
            res = A[i] + rec((i+1)%N, (j-1)%N)
        else:
            res = A[i] + rec((i+2)%N, j)
        # JOIが A[j] を選んだ場合
        # IOI は A[i] と A[(j-1)%N] のうち大きい方を取る
        if A[(j-1)%N] > A[i]:
            res = max(res, A[j] + rec(i, (j-2)%N))
        else:
            res = max(res, A[j] + rec((i+1)%N, (j-1)%N))
        dp[i][j] = res
        return res
 
    ans = max([rec(i, (i-1)%N) for i in range(N)])
    print(ans)
 
if __name__ == '__main__':
    main()


'''
## 最初に書いたコード
def rec(i, j, score):
    global dp
    if dp[i][j]:
        return dp[i][j] + score
    if j==i:
        dp[i][j] = A[i]
        return score + A[i]
    if j-i==1 or j-i==(-1)*(N-1):
        dp[i][j] = max(A[j], A[i])
        return score + max(A[j], A[i])
    ##rec(i+1, j, sore)
    if A[j] > A[(i+1)%N]:
        res = rec((i+1)%N, (j-1)%N, score+A[i])
    else:
        res = rec((i+2)%N, j, score+A[i])
    ##rec(i, j-1)
    if A[(j-1)%N] > A[i]:
        res = max(res, rec(i, (j-2)%N, score+A[j]))
    else:
        res = max(res, rec((i+1)%N, (j-1)%N, score+A[j]))
    dp[i][j] = res - score
    return res
 
ans = -1
if N <= 2:
    print(max(A))
    exit()
for i in range(N):
    #dp = dp2(0, N, N)
    if A[(i+1)%N] > A[(i-1)%N]:
        tmp = rec((i+2)%N, (i-1)%N, A[i])
    else:
        tmp = rec((i+1)%N, (i-2)%N, A[i])
    #tmp = rec(i, i, 0)
    #print(i, tmp)
    ans = max(ans, tmp)
print(ans)
'''

