A, B, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for i in range(M)]

ans = min(A)+min(B)

for i in range(M):
    if A[xyc[i][0]-1]+B[xyc[i][1]-1]-xyc[i][2] < ans:
        ans = A[xyc[i][0]-1]+B[xyc[i][1]-1]-xyc[i][2]

print(ans)