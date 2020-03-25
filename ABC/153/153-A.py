H, A = map(int,input().split())
ct = 0
while H>0:
    H -= A
    ct += 1
print(ct)