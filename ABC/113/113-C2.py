import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def ume(x):
    x = str(x)
    if len(x) < 6:
        return '0'*(6-len(x)) + x
    return x

def main():
    N, M = mi()

    l = li2(M)
    pos = [[] for _ in range(N+1)]
    ans = dp2(0, 2, M)

    for a, b in l:
        pos[a].append(b)
    for a in pos:
        a.sort()
    for i, a in enumerate(l):
        ind = bisect.bisect_left(pos[a[0]], a[1])
        l[i][1] = ind+1
        print(ume(l[i][0])+ume(l[i][1]))

if __name__ == "__main__":
    main()