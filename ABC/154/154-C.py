N = int(input())
A = sorted(map(int,input().split()))

for i in range(len(A)-1):
    if A[i]==A[i+1]:
        print('No')
        exit()

print('Yes')
    