N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

sum_list = [sum(A[0][0:i+1])+sum(A[1][i:N]) for i in range(N)]

print(max(sum_list))




