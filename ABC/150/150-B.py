N = int(input())
S = str(input())
'''
count = 0

if len(S) <= 2:
        print('0')
        exit(0)
elif len(S) == 3:
        if 'ABC' in S:
                print('1')
                exit(0)
else:
        for i in range(len(S)-3):
                if 'ABC' in S[i:i+3]:
                        count += 1

print(count)
'''
print(S.count('ABC'))