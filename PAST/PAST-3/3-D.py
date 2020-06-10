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

M = []

M.append([['###'], ['#.#'], ['#.#'], ['#.#'], ['###']]) #0

M.append([['.#.'], ['##.'], ['.#.'], ['.#.'], ['###']]) #1
 
M.append([['###'], ['..#'], ['###'], ['#..'], ['###']]) #2

M.append([['###'], ['..#'], ['###'], ['..#'], ['###']]) #3

M.append([['#.#'], ['#.#'], ['###'], ['..#'], ['..#']]) #4

M.append([['###'], ['#..'], ['###'], ['..#'], ['###']]) #5

M.append([['###'], ['#..'], ['###'], ['#.#'], ['###']]) #6

M.append([['###'], ['..#'], ['..#'], ['..#'], ['..#']]) #7

M.append([['###'], ['#.#'], ['###'], ['#.#'], ['###']]) #8

M.append([['###'], ['#.#'], ['###'], ['..#'], ['###']]) #9

N = ii()
S = [input() for _ in range(5)]
ans = ''

for i in range(N):
    for k in range(10):
        for j in range(5):
            if S[j][i*4+1:i*4+4] != M[k][j][0]:
                break
        else:
            ans += str(k)
print(ans)