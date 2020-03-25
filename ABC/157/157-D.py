class Unionfind:
    def __init__(self, n):
        self.d = [-1]*n
    
    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.find(self.d[x])
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True
    
    def same(self, x, y):
        if self.find(x)==self.find(y):
            return True
        return False
    
    def size(self, x):
        return (-1) * self.d[self.find(x)]

N, M, K = map(int,input().split())
deg = [0]*N
uf = Unionfind(N)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.unite(a, b)
    #print(uf.d)

for i in range(K):
    a, b = map(int, input().split())
    if uf.same(a-1, b-1)==True:
        deg[a-1] += 1
        deg[b-1] += 1

for i in range(N):
    #print(i, uf.d[i])
    #print(i, uf.size(i))
    print(uf.size(i)-1-deg[i])





