import sys
sys.setrecursionlimit(10**8)
#def main():　if __name__ == "__main__":　main()
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

S = input()
l = len(S)
d = defaultdict(int)

for c in S:
    d[c] += 1

d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
e = (d2[i][0] for i in range(len(d2)))

#alpha = [chr(i) for i in range(97, 97+26)]

ans = l
#for a in alpha:
for a in e:
    cnt = 0
    num_list = []
    for c in S:
        if c != a:
            cnt += 1
        else:
            num_list.append(cnt)
            cnt = 0
    num_list.append(cnt)
    ans = min(ans, max(num_list))

print(ans)