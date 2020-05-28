import sys

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

N, Q = map(int, input().split())

uf = Unionfind(N)

for i in range(Q):
    p, a, b = map(int, sys.stdin.readline().split())
    if p==0:
        uf.unite(a, b)
    else:
        if uf.same(a, b):
            print('Yes')
        else:
            print('No')


