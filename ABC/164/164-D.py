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
#from itertools import accumulate #list(accumulate(A))

S = list(map(int, list(input())))
mod = 2019

mod_list = [0]
ten = 1
for num in S[::-1]:
    yo = (num * ten + mod_list[-1]) % mod
    mod_list.append(yo)
    ten = (ten * 10) % mod

cnt = [0]*2019
for yo in mod_list:
    cnt[yo] += 1

ans = 0
for i in range(2019):
    ans += cnt[i] * (cnt[i]-1) // 2

print(ans)