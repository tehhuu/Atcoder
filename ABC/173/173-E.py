import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N, K = mi()
A = li()

d = defaultdict(int)
mod = 10**9+7
K_ = K

if N == K:
    ans = 1
    for num in A:
        ans *= num
        ans %= mod
    print(ans)
    exit()

for i in range(N):
    d[A[i]] += 1
    if A[i] < 0:
        A[i] *= -1

A = sorted(A, reverse=True)
l = []

for num in A:
    if d[-num] > 0:
        l.append(1)
        d[-num] -= 1
    else:
        l.append(0)
        d[num] -= 1

#print(l)
#print(sum(l[:K]))

if not sum(l[:K])%2:
    ans = 1
    for i in range(K):
        ans *= A[i]
        ans %= mod
    print(ans)

else:
    flag = False
    ans = 1
    for i in range(K, N):
        if not l[i]:
            flag = True
            ans *= A[i]
            ans %= mod
            break
    
    if flag:
        for i in reversed(range(K)):
            if flag and l[i]:
                flag = 0
                continue
            ans *= A[i]
            ans %= mod
        print(ans)
    
    else:
        if K%2:
            for i in range(N-K, N):
                ans *= A[i]
                ans %= mod
            ans *= -1
            ans %= mod
            print(ans)

        else:
            for i in range(N):
                if l[i]:
                    K -= 1
                    ans *= A[i]
                    ans %= mod
                if K == 0:
                    break

            else:
    
                ans = 1
                flag = True
                for i in reversed(range(K_)):
                    if flag and l[i]:
                        flag = 0
                        continue
                    ans *= A[i]
                    ans %= mod
                ans *= A[K_]
                ans %= mod
                print(ans)
                exit()

            print(ans)

