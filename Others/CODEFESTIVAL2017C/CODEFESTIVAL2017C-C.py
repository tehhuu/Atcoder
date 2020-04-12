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

## 前と後ろから探索

def main():
    S = input()
    l = len(S)

    T = S.replace('x', '')
    if T != T[::-1]:
        print(-1)
        exit()

    st, end = 0, l-1
    cnt = 0
    while True:
        if S[st] == S[end]:
            if st+1!=end:
                st += 1
                end -= 1
            else:
                st=end
        elif S[st] == 'x':
            st += 1
            cnt += 1
        elif S[end] == 'x':
            end -= 1
            cnt += 1
        if st==end:
            break
    print(cnt)
        
if __name__ == "__main__":
    main()
