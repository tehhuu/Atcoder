import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]

def bunkai(x):
    for i in reversed(range(1, int(x**0.5//1)+1)):
        #print(i)
        if x%i == 0:
            return list((i, x//i))
    return list((1, S))

S = ii()
lim = 10**9
s12 = S**0.5
a = int(s12)
keta = len(str(a))
b = 10**keta
if float(a)==s12:
    print(0, 0, a, 0, 0, a)
    exit()
#for i in range(a+1, b+1):
    #ii = i**2
    #if bunkai(ii)[0]<=lim and bunkai(ii)[1]<=lim and bunkai(ii-S)[0]<=lim and bunkai(ii-S)[1]<=lim:
        #print(0, 0, i, bunkai(ii-S)[1], bunkai(ii-S)[0], i)
        #exit()
print(0, 0, a+1, bunkai((a+1)**2-S)[1], bunkai((a+1)**2-S)[0], a+1)