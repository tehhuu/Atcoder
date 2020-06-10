x1, y1, x2, y2 = map(int, input().split())
 
ans = ''
 
dx = x2 - x1
dy = y2 - y1
 
ans += 'R'*dx + 'U'*dy + 'R' + 'D'*(dy+1) + 'L'*(dx+1) + 'U'*(dy+1) + 'R'*dx + 'U' + 'L'*(dx+1) + 'D'*(dy+1) + 'R'
 
print(ans)