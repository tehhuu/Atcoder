N, K = map(int,input().split())
P = list(map(float,input().split()))
for i in range(N):
    P[i] = (P[i]+1.0)/2.0

anss=0        
for i in range(N-K+1):
    #print(i)
    #ans_kari = sum(P[i:i+K])
    if i==0:
        ans_kari = sum(P[i:i+K])
    else:
        ans_kari = ans_kari - P[i-1] + P[i+K-1]
    #print(ans_kari)
    #print(i)
    if ans_kari > anss:
        anss = ans_kari

print(anss)