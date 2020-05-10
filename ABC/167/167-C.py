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

# BIT全探索

N, M ,X = mi()
CA = [li() for _ in range(N)]

B = 2**N
ans = float('inf')
for i in range(B):
    cnt = [0]*M
    flag = 1
    kane = 0
    for j in range(N):
        if i & 1 << j:
            kane += CA[j][0]
            for k in range(M):
                cnt[k] += CA[j][k+1]
    for k in range(M):
        if cnt[k] < X:
            flag = 0
            break
    if flag:
        ans = min(ans, kane)
if ans == float('inf'):
    print(-1)
    exit()
print(ans)
            
