N = int(input())
A = list(map(int, input().split()))
'''
seki = 1
#全要素の積を求めてから2で割り続けたらTLEになった。
for a_i in A:
        seki *= a_i

count = 0

while seki % 2 == 0:
        seki = seki // 2
        count += 1
'''

count = 0

for a_i in A:
        while a_i % 2 == 0:
                a_i = a_i // 2
                count += 1

print(count)