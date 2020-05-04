import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
import itertools

def nishin(x):
    x_ni = bin(x)[2:]
    if len(x_ni) < 7:
        return '0'*(7-len(bin(x)[2:])) + x_ni
    else:
        return x_ni

def xor(x, y):
    ans = ''
    for i,j in x, y:
        if i == j:
            ans += '0'
        else:
            ans += '1'
    return ans

def xor_list(l):
    ans = xor(l[0], l[1])
    for i in range(2, len(l)):
        ans = xor(ans, l[i])
    return ans


N, K = mi()
T = li2(N)

for i in range(N):
    for j in range(K):
        T[i][j] = nishin(T[i][j])

if N == 1:
    if '0000000' in T[0]:
        print('Found')
        exit()

elif N == 2:
    for i, j in itertools.product(range(K), range(K)):
        if xor_list([T[0][i], T[1][j]]) == '0000000':
            print('Found')
            exit()

elif N == 3:
    for i, j, k in itertools.product(range(K), range(K), range(K)):
        if xor_list([T[0][i], T[1][j], T[2][k]]) == '0000000':
            print('Found')
            exit()

elif N == 4:
    for i, j, k, l in itertools.product(range(K), range(K), range(K), range(K)):
        if xor_list([T[0][i], T[1][j], T[2][k], T[3][l]]) == '0000000':
            print('Found')
            exit()

else:
    for i, j, k, l, m in itertools.product(range(K), range(K), range(K), range(K), range(K)):
        if xor_list([T[0][i], T[1][j], T[2][k], T[3][l], T[4][m]]) == '0000000':
            print('Found')
            exit()

print('Nothing')









