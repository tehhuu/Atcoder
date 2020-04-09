import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

import heapq
def dijkstra_heap(s, edge):
    #始点sから各頂点への最短距離
    ###[e[0]:コスト, e[1]：目的地]
    d = [float("inf")] * N      #各頂点への最小距離を記憶
    used = [True] * N           #True:未確定
    d[s] = 0                    #スタート地点は0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)         #スタート地点につながった頂点をプッシュ
    while len(edgelist):
        minedge = heapq.heappop(edgelist)   #一番距離が小さいものを取り出す
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:            #既に最短距離確定済みだったらスルー
            continue
        v = minedge[1]                      
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                if e[0]+d[v] > d[e[1]]:                     #既に求まってる最短距離以上なら枝刈り
                    continue
                heapq.heappush(edgelist, [e[0]+d[v], e[1]]) #最小値更新した頂点につながった頂点をプッシュ
    return d


N, M, T = mi()
A = li()

edge_f = [[] for i in range(N)]
edge_b = [[] for i in range(N)]
for i in range(M):
    a, b, c = mi()
    edge_f[a-1].append([c, b-1])
    edge_b[b-1].append([c, a-1])

t_f = dijkstra_heap(0, edge_f)
t_b = dijkstra_heap(0, edge_b)

ans = 0
for i in range(N):
    ans = max(ans, A[i]*(T - t_f[i] - t_b[i]))

print(ans)


        
    
    

