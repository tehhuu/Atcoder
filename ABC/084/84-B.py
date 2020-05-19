import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())

A, B = mi()
S = input()
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if S[A] != '-':
    print('No')
    exit()

for i in range(A+B+1):
    if i != A and S[i] not in number:
        print('No')
        exit()

print('Yes')

