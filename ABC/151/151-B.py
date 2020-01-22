N, K, M = map(int,input().split())
A = list(map(int,input().split()))

s = sum(A)
if M*N-s < 0:
        print(0)
elif M*N-s > K:
        print('-1')
else:
        print(M*N-s)