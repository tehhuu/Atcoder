import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
S = input()

flag_m = [0]*(N)
flag_p = [0]*(N)
keta_list_m = [0]*(N)
keta_list_p = [0]*(N)

mod = S.count('1')

if mod == 1:
    flag_p[-1] = int(S[-1]) % (mod+1)
    keta_list_p[-1] = 1 % (mod+1)
    keta_p = 1
    for i in reversed(range(N-1)):
        keta_p *= 2
        keta_p %= (mod+1)
        keta_list_p[i] = keta_p
        if S[i] == '1':
            flag_p[i] = keta_p
    sum_f_p = sum(flag_p)

    for i in range(N):
        if S[i] == '1':
            print(0)
            continue
        else:
            num = (sum_f_p + keta_list_p[i]) % (mod+1)
    
        ans = 1
        if num == 0:
            print(ans)
            continue

        while True:
            cnt = 0
            tmp = 0
            while (1 << tmp) <= num:
                if num & 1 << tmp:
                    cnt += 1
                tmp += 1
            num %= cnt
            ans += 1
            if num == 0:
                print(ans)
                break
    exit()

flag_p[-1] = int(S[-1]) % (mod+1)
flag_m[-1] = int(S[-1]) % (mod-1)
keta_list_p[-1] = 1 % (mod+1)
keta_list_m[-1] = 1 % (mod-1)
keta_m = 1
keta_p = 1
for i in reversed(range(N-1)):
    keta_m *= 2
    keta_m %= (mod-1)
    keta_p *= 2
    keta_p %= (mod+1)
    keta_list_m[i] = keta_m
    keta_list_p[i] = keta_p
    if S[i] == '1':
        flag_p[i] = keta_p
        flag_m[i] = keta_m

sum_f_m = sum(flag_m)
sum_f_p = sum(flag_p)

for i in range(N):
    if S[i] == '1':
        num = (sum_f_m - keta_list_m[i]) % (mod-1)
    else:
        num = (sum_f_p + keta_list_p[i]) % (mod+1)

    ans = 1
    if num == 0:
        print(ans)
        continue

    while True:
        cnt = 0
        tmp = 0
        while (1 << tmp) <= num:
            if num & 1 << tmp:
                cnt += 1
            tmp += 1
        num %= cnt
        ans += 1
        if num == 0:
            print(ans)
            break
        