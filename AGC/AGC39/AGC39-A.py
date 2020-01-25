a, b = map(int, input().split())

a_0 = a // 100
b_0 = b // 100

if a_0 != 9 or b_0 != 1:
        print(a-b + max(9-a_0,b_0-1)*100)

elif (a%100)//10 != 9 or (b%100)//10 != 0:
        print(a-b + max(9-(a%100)//10, (b%100)//10-0)*10)

else:
        print(a-b + max(9-a%10, b%10-0))
