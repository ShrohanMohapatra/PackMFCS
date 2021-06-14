#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:53:47 2021

@author: shrohanmohapatra
"""

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
        root = x
        while self.forest[root]['parent']!=root:
            root = self.forest[root]['parent']
        while self.forest[x]['parent']!=root:
            parent = self.forest[x]['parent']
            self.forest[x]['parent'] = root
            x = parent
        return root
    def UnionBySize(self,x,y):
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        self.forest[x] = self.forest[xRoot]
        self.forest[y] = self.forest[yRoot]
        if self.forest[x] == self.forest[y]: return
        if self.forest[x]['size'] < self.forest[y]['size']:
            (self.forest[x],self.forest[y]) = (self.forest[y], \
                                               self.forest[x])
        self.forest[y]['parent'] = x
        self.forest[x]['size'] = self.forest[x]['size'] + \
            self.forest[y]['size']
    def UnionByRank(self,x,y):
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        self.forest[x] = self.forest[xRoot]
        self.forest[y] = self.forest[yRoot]
        if self.forest[x] == self.forest[y]: return
        if self.forest[x]['rank'] < self.forest[y]['rank']:
            (self.forest[x],self.forest[y]) = (self.forest[y], \
                                               self.forest[x])
        self.forest[y]['parent'] = x
        self.forest[x]['rank'] = self.forest[x]['rank'] + 1

# Some elementary basic checks whether they work with the code
# that works for the class definition

print('Some elementary basic checks ...')
A = {1:'a',2:'b',3:'c'}
B = {1:'a',2:'b',3:'d'}
print(A==B)
B = A
print(A==B)
a = 4
b = 6
print(a,b)
(a, b) = (b, a)
print(a,b)

print('Now let us test the disjoint set data structure ...')
newMarrion = disjointSetNew()
for k in range(1,11):
    print('Adding k =',k,' to the set!')
    newMarrion.MakeSet(k)
print(newMarrion.forest)
for k in range(1,5):
    print('Unifying',2*k-1,'and',2*k)
    newMarrion.UnionBySize(2*k-1, 2*k)
from time import time
for k in range(1,11):
    start = time()
    s1 = newMarrion.Find(k)
    end = time()
    print('Finding ',k,'and found',s1)
    print('Time taken = ',(end-start)*10**6,'usecs')
