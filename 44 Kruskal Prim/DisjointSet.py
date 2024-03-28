#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
print(ds.vertices)
print(ds.parent)
print(ds.rank)
print()
ds.union("A", "B")
print(ds.vertices)
print(ds.parent)
print(ds.rank)
print()
ds.union("A", "C")
print(ds.vertices)
print(ds.parent)
print(ds.rank)
print()
print(ds.find("A"))