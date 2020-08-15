import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
from itertools import combinations

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    return is_prime 
    #table = [ i for i in range(1, n+1) if is_prime[i-1]]
    #return is_prime, table


N = ii()
a = [3, 5, 7, 11, 31]
is_prime = sieve(300000)
tmp = 37

for i in range(N-5):
    while True:
        if is_prime[tmp]:
            if tmp > 55555:
                print(len(a))
                print('No')
                exit()
            for c in combinations(a, 4):
                if is_prime[tmp+sum(c)]:
                    break
            else:
                a.append(tmp)
                break
        tmp += 1

print(a)