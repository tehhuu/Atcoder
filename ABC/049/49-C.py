S = input()[::-1]

kari = ['dream', 'dreamer', 'erase', 'eraser']
 
words = [i[::-1] for i in kari]
 
l = len(S)
cnt = ''

for i in range(l):
    cnt += S[i]
    if cnt in words:
        cnt = ''

if cnt!='':
    print('NO')
else:
    print('YES')