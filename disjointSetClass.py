class disjointSetNew:
    def __init__(self):
        self.forest = {}
    def MakeSet(self,x):
        if x not in self.forest:
            self.forest[x] = {}
            self.forest[x]['parent'] = x
            self.forest[x]['size'] = 1
            self.forest[x]['rank'] = 0
    def Find(self, x):
        root = self.forest[x]
        while root['parent']!=root:
            root = self.forest[root['parent']]
        while self.forest[x]['parent']!= root:
            parent = self.forest[x]['parent']
            self.forest[x]['parent'] = root
            self.forest[x] = parent
        return root
    def UnionBySize(self,x,y):
        x = self.Find(self,x)
        y = self.Find(self,y)
    # To be written by union by size or union by root ....
