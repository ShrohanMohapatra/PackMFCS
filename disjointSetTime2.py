#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:06:42 2021

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

numberOfElements = 600
newMarrion = disjointSetNew()
for k in range(1,numberOfElements+1):
    print('Adding k =',k,' to the set!')
    newMarrion.MakeSet(k)
for k in range(1,int(numberOfElements/2)+1):
    if 2*k-1 in newMarrion.forest and 2*k in newMarrion.forest:
        newMarrion.UnionBySize(2*k-1, 2*k)
for k in range(int(numberOfElements/4)):
    if 4*k+1 in newMarrion.forest and 4*k+3 in newMarrion.forest:
        newMarrion.UnionBySize(4*k+1, 4*k+3)
from time import time
for k in range(1,numberOfElements+1):
    start = time()
    s1 = newMarrion.Find(k)
    end = time()
    print('Finding ',k,'and found',s1)
    print('Time taken = ',(end-start)*10**6,'usecs')


