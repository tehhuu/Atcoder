import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
import math
 
N, K = mi()
A = li()

if K == 0:
    print(max(A))
    exit()

left = 0
right = max(A)
 
def count(num):
    cnt = 0
    for i in range(N):
        cnt += math.ceil(A[i] / num) - 1
    return cnt
'''
while True:
    mid = (left + right) // 2
    if mid == 0:
        print(1)
        break
    tmp = count(mid)
    if right - left <= 1:
        print(right)
        exit()
    elif tmp > K:
        left = mid
    else:
        right = mid
'''

def is_ok(arg):
    if count(arg) <= K:
        return True
    else:
        return False
    

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, right+1))