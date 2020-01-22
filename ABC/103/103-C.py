'''
#全てのmに対してf(m)を調べようとしたらTLEになった
def f(m, a):
        ans = 0
        for a_i in a:
                ans += m % a_i
        return ans

N = int(input())
a = list(map(int, input().split()))

ans_list = [f(i, a) for i in range(2,10**7+1)]

print(max(ans_list))
'''

N = int(input())
a = list(map(int, input().split()))

print(sum(a)-N)