class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
        self.num_components = n

    
    def _ensure(self, n) -> None:
        if n not in self.parent:
            self.parent[n] = n
        if n not in self.rank:
            self.rank[n] = 0


    def find(self, x: int) -> int:
        self._ensure(x)
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        
        p1 = self.find(x)
        p2 = self.find(y)

        # Same component
        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1
        
        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        return self.num_components