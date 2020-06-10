import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
import heapq

N = ii()
A = []
cnt = [0] * N
for _ in range(N):
    #N, *A = mi()
    #l = li()
    A.append(li())
M = ii()
M_list = li()

l_1 = []
l_2 = []
d = defaultdict(int)
for i in range(N):
    a1 = -A[i][1]
    l_1.append(a1)
    d[a1] = i
    if A[i][0] > 1:
        a2 = -A[i][2]
        l_2.append(a2)
        d[a2] = i

heapq.heapify(l_1)
heapq.heapify(l_2)

for num in M_list:
    #print(cnt)
    if num == 1:
        ans = heapq.heappop(l_1)
        i = d[ans]
        if cnt[i]+1 < A[i][0]:
            heapq.heappush(l_1, -A[i][cnt[i]+1])
            cnt[i] += 1
            d[-A[i][cnt[i]+1]] = i
        
    else:
        ans = heapq.heappop(l_2)
        i = d[ans]
        if cnt[i]+2 < A[i][0]:
            heapq.heappush(l_2, -A[i][cnt[i]+2])
            cnt[i] += 1
            d[-A[i][cnt[i]+2]] = i
        if A[i][cnt[i]-1] == ans:
            heapq.heappush(l_1, -A[i][cnt[i]+1])
            d[-A[i][cnt[i]+1]] = i
    print(-ans)
