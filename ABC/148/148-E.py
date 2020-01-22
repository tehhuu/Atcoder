'''
import sys
A = 10**18
sys.setrecursionlimit(A)

N = int(input())

def f(N):
    if N % 2 == 1:
        n = (N+1)//2
        if n == 1:
            return 1
        else:
            return (2*n+1) * f(2*(n-1))
        
    else:
        n = N // 2
        if n == 1:
            return 1
        else:
            return 2 * n * f(2*(n-1))


count = 0
a = f(N)
print(a)

while(a % 10 ==0):
    a = a // 10
    count += 1

print(count)


#N = int(input())
'''
'''
N = int(input())

if N % 2 == 1:
    print('0')

else:
'''
'''
N = int(input())
count = 0


if N % 2 == 0:
    n = N
    sho = n // 10
    #print(sho)
    for i in range(1, sho+1):
        k = i * 10
        #print(k)
        while(k % 5 == 0 and k > 0):
            #print(k)
            k = k // 5
            count += 1

print(count)
'''

N = int(input())
count = 0
k = 5

if N % 2 == 0:
    n = (N // 2 // 5) * 5
    while(n >= k):
        count += n // k
        k *= 5

print(count)