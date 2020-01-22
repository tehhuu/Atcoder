S = str(input())
K = int(input())
'''
#単純に左から調べようとしたらTLEになった。
gosencho = 5 * (10**15)

for i in S:
        print(i)
        #K -= int(i) ** gosencho
        K -= pow(int(i), gosencho)
        if K <= 0:
                print(i)
                exit(0)
'''
'''
ans = ''
for i in S:
        for j in range(int(i)**gosencho):
                ans += i

print(ans[K])
'''
if len(S) == 1:
        print(S[0])
        exit(0)

i = 0
while S[i] == '1' and i <= len(S)-2:
        if K <= i + 1:
                print(S[i])
                exit(0)
        i += 1
print(S[i])

