N, A, B= map(int,input().split())

if N % (A+B) > A:
    print(N // (A+B) * A + A)
    exit()
print(N // (A+B) * A + N % (A+B))




                        