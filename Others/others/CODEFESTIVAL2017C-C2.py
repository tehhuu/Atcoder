import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

## ランレングス圧縮みたいな

def main():
    S = input()
    l = len(S)

    T = S.replace('x', '')
    if T != T[::-1]:
        print(-1)
        exit()

    zero_list = []
    cnt = 0
    for i in range(l):
        if S[i] == 'x':
            cnt += 1
        elif i>0:
            zero_list.append(cnt)
            cnt = 0
        elif i==0:
            zero_list.append(cnt)
    zero_list.append(cnt)

    lz = len(zero_list)
    ans = 0
    for i in range(lz//2):
        ans += abs(zero_list[i] - zero_list[lz-1-i])
    print(ans)
        
if __name__ == "__main__":
    main()
