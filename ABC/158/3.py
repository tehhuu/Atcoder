def mpow(x: int, k: int, MOD=1000000007) -> int:
    """
    x^kのmodを返します
    """
    res = 1
    y = x
    while (k):
        if(k % 2 == 1):
            res = (res * y) % MOD
        y = (y ** 2) % MOD
        k = k // 2
    return res
'''
def cmb(n, x, mod=10**9+7):
    # nCx
    # 組み合わせ
    # ex) combination(5, 2) = 10
    factorial = [1] * (n+1)
    t = 1
    for i in range(1, n+1):
        t = (t * i) % mod
        factorial[i] = t
    tmp = factorial[n]
    tmp = (tmp * pow(factorial[x], mod-2, mod)) % mod
    tmp = (tmp * pow(factorial[n-x], mod-2, mod)) % mod
    return tmp
'''
mod = 10**9+7 #出力の制限

N, a, b = map(int,input().split())

print(mpow(2,10**9))

num = 1000000000 + 7

MAX_NUM = N
MOD = 10**9+7

fac  = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv  = [0 for _ in range(MAX_NUM)]

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,MAX_NUM):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def cmb(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

#print(mpow(2,N))

print(mpow(2,N)- cmb(N, a) - cmb(N, b) -1)


