# coding=utf-8


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

import sys
w = 79
h = 23
d = 1.0/(h+1)
if len(sys.argv)>1:
    h = int(sys.argv[1])-1
    d = 1.0/(h+1)
    if len(sys.argv)>2:
        w = int(sys.argv[2])-1
        if len(sys.argv)>3:
            d = float(sys.argv[3])/(h+1)
l = connectionSetThing(w)

walls = '━┃'
corners = '┏┓┗┛┣┫┳┻╋'
def getCornerWalls(n):
    # 0
    #3+1
    # 2
    w= ['•','╹','╺','┗','╻','┃','┏','┣','╸','┛','━','┻','┓','┫','┳','╋']
    return w[n]
def getCorner(a,b,c,d):
    #a b
    # +
    #c d
    if a == b:
        if a == c:
            if a == d:
                return '•'
            else:
                return '┏'
        else:
            if a == d:
                return '┓'
            else:
                if c == d:
                    return '━'
                else:
                    return '┳'
    else:
        if a == c:
            if a == d:
                return '┗'
            else:
                if b == d:
                    return '┃'
                else:
                    return '┣'
        else:
            if a == d:
                return '╋'
            else:
                if b == c:
                    if b == d:
                        return '┛'
                    else:
                        if c == d:
                            return '┻'
                        else:
                            return '╋'
                else:
                    if b == d:
                        return '┫'
                    else:
                        if c == d:
                            return '┻'
                        else:
                            return '╋'

def mazeStepWalls(l,isLast=False):
    s = '| '
    for i in range(w-1):
        if (random()<.5 or isLast) and not( l.connected(i,i+1)):
            l.connect(i,i+1)
            s += '  '
        else:
            s += '| '
    return s + '|'
def mazeStepDown(l,isLast=False):
    s = '+'
    for i in range(w):
        if (random()<.5 and not (l.isOnly(i))) or isLast:
            l.disconnect(i)
            s += '-'
        else:
            s += ' '
        s += '+'
    return s
        
                        
from random import random
from time import sleep

oldwalls = '  '*w+' '
down = ' '+'+-'*w+'+ '
for row in range(h+1):
    sleep(d)
    walls = mazeStepWalls(l,row + 1 == h)       #ex:  '|   |'
    #fwall = ''
    #fdown = ''
    #for i in range(2*w+1):
    #    if i%2:
    #        fdown += [' ','━'][down[i+1] != ' ']
    #        fwall += ' '
    #    else:
    #        fdown += getCornerWalls((oldwalls[i] != ' ')+2*(down[i+2] != ' ')+4*( walls[i] != ' ')+8*(down[i] != ' '))
    #        fwall += [' ','┃'][walls[i] != ' ']
    f = ''
    for i in range(w+1):
        f += getCornerWalls((oldwalls[2*i] != ' ')+2*(down[2*i+2] != ' ')+4*( walls[2*i] != ' ' and row != h)+8*(down[2*i] != ' '))
    
    down = ' '+mazeStepDown(l,row + 1 == h)+' ' #ex: ' +-+ + '
    #print(fdown)
    #print(fwall)
    print(f)


    
    oldwalls = walls
        



    

            

            
