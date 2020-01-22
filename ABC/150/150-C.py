import itertools

N = int(input())
P = list(map(str,input().split()))
Q = list(map(str,input().split()))

A = sorted(P)
count=0

for v in itertools.permutations(A, N):
    if P == list(v):
        p_cou = count
    if Q == list(v):
        q_cou = count
    count += 1

print(abs(q_cou-p_cou))