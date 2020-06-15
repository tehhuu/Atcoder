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

N = ii()
A = sorted(li())
max_a = A[-1]

flag = [0] * (A[-1]+1)
cnt = 0

for i, num in enumerate(A):
    if i == N-1 and not flag[num]:
        cnt += 1
    elif not flag[num] and A[i+1] != num:
        cnt += 1
    x = num
    while True:
        flag[x] = 1
        x += num
        if x > max_a:
            break

print(cnt)