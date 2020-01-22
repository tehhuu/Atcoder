A, B, K = map(int, input().split())
flag = 0

if K >= A:
        K -= A
        A = 0
        flag = 1

if flag == 1 and K >= B:
        K -= B
        B = 0

if A == 0 and B == 0:
                print('0 0')
                exit(0)
        
if A > 0:
        print(A-K, B)
        exit(0)
        
if B > 0:
        print(A, B-K)