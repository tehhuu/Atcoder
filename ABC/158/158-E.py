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

N, mod = mi()
S = list(map(int, list(input())))
ans = 0

if 10 % mod != 0:
    mod_list = [0]
    ten = 1
    for num in S[::-1]:
        yo = (num * ten + mod_list[-1]) % mod
        mod_list.append(yo)
        ten = (ten * 10) % mod

    cnt = [0]*mod
    for yo in mod_list:
        cnt[yo] += 1

    for i in range(mod):
        ans += cnt[i] * (cnt[i]-1) // 2

else:
    for i, num in enumerate(S):
        if num % mod == 0:
            ans += i+1

print(ans)