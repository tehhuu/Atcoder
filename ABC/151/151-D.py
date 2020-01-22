H, W = map(int,input().split())
A = [list(input()) for i in range(H)]

#from queue import Queue #キューを使ったら1ケースだけTLEになった。
from collections import deque

dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

sum_sharp = sum([A[i].count('#') for i in range(H)])

fin_d_max = 1

for s_i in range(H):
    for s_j in range(W):
        d_max = 0
        #q_i = Queue()
        q_i = deque()
        #q_j = Queue()
        q_j = deque()
        D = [[-1]*W for i in range(H)]
        flag = 1

        if A[s_i][s_j] == '.':
            D[s_i][s_j] = 0
            #q_i.put(s_i)
            q_i.append(s_i)
            #q_j.put(s_j)
            q_j.append(s_j)
            #while q_i.empty() == False:
            while len(q_i)!=0:
                #i = q_i.get()
                i = q_i.popleft()
                #j = q_j.get()
                j = q_j.popleft()
                for x in range(4):
                    ni = i+di[x]
                    nj = j+dj[x]
                    if ni<0 or ni>=H or nj<0 or nj>=W or A[ni][nj]== '#' or D[ni][nj]!=-1:
                        continue
                    else:
                        flag += 1
                        D[ni][nj] = D[i][j]+1
                        d_max = max(d_max, D[ni][nj])
                        #q_i.put(ni)
                        q_i.append(ni)
                        #q_j.put(nj)
                        q_j.append(nj)
        fin_d_max = max(fin_d_max, d_max)
                
print(fin_d_max)
                    
            
        