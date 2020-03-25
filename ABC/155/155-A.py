A, B, C = sorted(map(int,input().split()))

if A==B==C:
    print('No')
elif A==B or B==C:
    print('Yes')
else:
    print('No')