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
'''
#全探索
S = input()
n = len(S)

ans_0 = '01'*(n//2) + '0'*(n%2)
ans_1 = '10'*(n//2) + '1'*(n%2)

c_0 = c_1 = 0

for i in range(n):
    if ans_0[i] != S[i]:
        c_0 += 1
    if ans_1[i] != S[i]:
        c_1 += 1

print(min(c_0, c_1))
'''
#ビット演算を利用
S = list(map(int, input()))
n = len(S)
a = 0
cnt_0 = cnt_1 = 0
for moji in S:
    cnt_0 += moji ^ a
    a ^= 1

a = 1
for moji in S:
    cnt_1 += moji ^ a
    a ^= 1

print(min(cnt_0, cnt_1))