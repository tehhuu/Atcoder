A, B, K = map(str, input().split())

for i in range(K):
        if A > 0:
                A -= 1
        elif B > 0:
                B -= 1
        else:
                exit(0)

print(A, B)