A, B = list(map(int, sys.stdin.readline().split()))

if A == B == 1:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
else:
    if A > B:
        print('Alice')
    elif B > A:
        print('Bob')
    else:
        print('Draw')