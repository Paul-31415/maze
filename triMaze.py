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
        if 0 <= i < len(self.dat):
            return not (self.dat[i] in self.dat[:i] or self.dat[i] in self.dat[i+1:])
        return False
        
    def list(self):
        return self.dat
    def __repr__(self):
        return 'cst('+str(self.dat)+')'
    def __len__(self):
        return len(self.dat)



w = 16
h = 8

import sys
if len(sys.argv)>1:
    h = int(sys.argv[1])
    if len(sys.argv)>2:
        w = int(sys.argv[2])


#O---O---O---O---O---O---O
# \   \   \       \     / \
#  O   O   O   O---O   O   O
# /       /   /     \     /
#O   O   O   O   O   O   O
# \ /         \ /         \
#  O   O   O---O   O   O---O
# /     \ /         \     /
#O   O---O   O---O   O---O
# \   \     /   /   /   / \
#  O   O   O   O   O   O   O
# /         \   \ /       /
#O   O   O   O   O   O   O
# \   \   \           \   \
#  O---O---O---O---O---O---O
wp = 1-1./3
sdp= 1./3

def mazeStepWalls(l,card,isLast=False): #  \ / \ / part
    s = [' \\',' /'][card]
    c = [' /',' \\']
    
    for i in range(w-1):
        if (random()<wp or isLast or (i%2 == card and l.isOnly(i)) or (w%2!=card and i == w-2 and l.isOnly(i+1))    ) and not( l.connected(i,i+1)):
            l.connect(i,i+1)
            s += '  '
        else:
            s += c[(i+card)%2]
    return s + c[(w-1+card)%2]

def CardNumIn(l,i,c):
    return sum([v == l[i] for v in l.dat[c::2]])

def mazeStepDown(l,c,isLast=False): #O---O---O part
    #
    s = ['  O','O'][c]
    for i in range(w):
        if i%2 != c:
            if (random()<sdp and not (CardNumIn(l,i,c^1)==1)) or isLast:
                l.disconnect(i)
                s += '---O'
            else:
                s += '   O'
        else:
            l.disconnect(i)
    return s

print('O'+'---O'*(w//2+(w&1)))
l = connectionSetThing(w)
for row in range(h):
    print(mazeStepWalls(l,row%2,row + 1 == h))
    print(mazeStepDown(l,row%2, row + 1 == h))

#print(['  O','O'][h%2]+'---O'*((w//2)+h%2))
