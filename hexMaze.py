# coding=utf-8
from random import random
class connectionSetThing:
    def __init__(self,l):
        self.dat = [i for i in range(l)]
    def __getitem__(self,i):
        if i < 0 or i >= len(self.dat):
            return -1
        return self.dat[i]
    def disconnect(self,i):
        self.dat[i] = -1
        self.dat[i] = max(self.dat)+1
    def connect(self,a,b):
        if self.dat[b] < self.dat[a]:
            a,b = b,a
        v = self.dat[b]
        
        for i in range(len(self.dat)):
            if self.dat[i] == v:
                self.dat[i] = self.dat[a]
    
    def connected(self,a,b):
        return self.dat[a] == self.dat[b]

    def isLast(self,i):
        return not (self.dat[i] in self.dat[i+1:])

    def isOnly(self,i):
        return not (self.dat[i] in self.dat[:i] or self.dat[i] in self.dat[i+1:])
        
    def list(self):
        return self.dat
    def __repr__(self):
        return 'cst('+str(self.dat)+')'
    def __len__(self):
        return len(self.dat)


# _/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\_/¯\
#/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
#\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
#/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   yes.
#\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \
#/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
#\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 


#/\/\/\/\/\/\/\/\/\/\/\/\/\
#| | | | | | | | | | | | | |
#\/\/\/\/\/\/\/\/\/\/\/\/\/    no.
# | | | | | | | | | | | | |
#/\/\/\/\/\/\/\/\/\/\/\/\/\

w = 16
h = 8

import sys
if len(sys.argv)>1:
    h = int(sys.argv[1])
    if len(sys.argv)>2:
        w = int(sys.argv[2])

def mazeStepWalls(l,card,isLast=False): #setwise almost the same as square
    s = ['/','\\'][card]
    c = [' \\',' /']
    
    for i in range(w-1):
        if (random()<2.0/3 or isLast) and not( l.connected(i,i+1)):
            l.connect(i,i+1)
            s += '  '
        else:
            s += c[(i+card)%2]
    return s + c[(w-1+card)%2]

def mazeStepDown(l,c,isLast=False): 
    #_
    s = ''
    for i in range(w):
        if i%2 != c:
            if (random()<2.0/3 and not (l.isOnly(i))) or isLast:
                l.disconnect(i)
                s += '_'
            else:
                s += ' '
    return s

print(' '+'_/¯\\'*(w//2)+ ['','_'][w%2])
l = connectionSetThing(w)
for row in range(h):
    walls = mazeStepWalls(l,row%2,row + 1 == h)
    down = mazeStepDown(l,row%2, row + 1 == h)
    
    combined = ''
    for i in range(len(walls)):
        if i%4 == [3,1][row%2]:
            combined += down[i//4]
        else:
            combined += walls[i]

    print(combined)
print(['  ',''][h%2]+'\\_/ '*((w//2)+h%2))
