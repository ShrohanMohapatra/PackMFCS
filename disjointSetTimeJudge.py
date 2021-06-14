#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:54:57 2021

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

from random import randint

numberOfElements = 40
M = 10 # The number of union operations
newMarrion = disjointSetNew()
for k in range(1,numberOfElements+1):
    print('Adding k =',k,' to the set!')
    newMarrion.MakeSet(k)
for k in range(M):
    while True:
        x = randint(1,numberOfElements)
        y = randint(1,numberOfElements)
        if x!=y or newMarrion.forest[x]['parent'] == y \
            or newMarrion.forest[y]['parent'] == x:
            break
    print("Unification -> ",x, y)
    if newMarrion.forest[y]['parent'] != x:
        newMarrion.UnionByRank(x, y)
from time import time
for k in range(1,numberOfElements+1):
    start = time()
    s1 = newMarrion.Find(k)
    end = time()
    print('Finding ',k,'and found',s1)
    print('Time taken = ',(end-start)*10**6,'usecs')


