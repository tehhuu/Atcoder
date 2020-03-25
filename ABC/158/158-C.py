
import fractions

A, B = map(int,input().split())

for i in range(1, 2000):
        #if fractions.floor(i * 0.08)==A:
        if (i*0.08)//1 == float(A) and (i*0.1)//1 == float(B):
                print(i)
                exit()
print('-1')


##print((26*0.08)//1)





