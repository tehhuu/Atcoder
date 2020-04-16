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

## スタックを利用
from collections import deque
ans = deque()

for m in S:
    if m == 'S':
        ans.append(m)
    elif m == 'T':
        if ans and ans[-1] == 'S':
            ans.pop()
        else:
            ans.append(m)
print(len(ans))

'''
##　スタックを用いずにカウント
s_cnt = 0
for m in S:
    if m == 'S':
        s_cnt += 1
    elif m == 'T' and s_cnt > 0:
        s_cnt -= 1

print(2 * s_cnt)
'''