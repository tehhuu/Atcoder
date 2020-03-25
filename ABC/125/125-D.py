N = int(input())

A = sorted(list(map(int, input().split())))
'''
###全探索
INF = 10**6

ind = INF
for i in range(len(A)):
    if A[i]>=0:
        ind = i
        break
    else:
        A[i] *= -1

if ind == INF:
    ind = N

if ind %2 == 0:
    print(sum(A))
elif ind==N:
    print(sum(A)-2*A[ind-1])
else:
    print(sum(A)-2*min(A[ind], A[ind-1]))
'''

#二分探索
start = 0
end = N-1

while end != start:
    if A[(start+end)//2] >= 0:
        end = (start+end)//2
    elif end-start==1:
        start = (start+end)//2+1
    else:
        start = (start+end)//2

if start==N-1 and A[N-1]<0:
    start=N

if start%2==0:
    print(sum(A[:start])*(-1) + sum(A[start:]))
elif start==N:
    print(sum(A[:start])*(-1) + sum(A[start:]) + 2*A[N-1])
else:
    print(sum(A[:start])*(-1) + sum(A[start:]) - 2*min(A[start], (-1)*A[start-1]))



    

