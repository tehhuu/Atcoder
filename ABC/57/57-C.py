N = int(input())

#print(int((N**0.5)//1))
for i in range(min(int((N**0.5)//1)+1, 10**5), 0, -1):
    if N % i == 0:
        #print(i)
        print(max(len(str(i)), len(str(N//i))))
        exit()