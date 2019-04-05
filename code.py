#Fannar Hrafn Haraldsson
#!/usr/bin/env python
# -*- coding: utf-8 -*-



#heildun og flatarmál
import math
fall1=input("sláðu inn fall f(x): ")
fall2=input("sláðu inn fall g(x): ")
emork=input("sláðu inn x fyrir efri mörk: ")
nmork=input("sláðu inn y fyrir neðri mörk: ")
def heildun(emork,nmork,fall):
    currefra = int(emork)
    currnedra = int(nmork)
    for z in range(len(fall)):
        margfeldi = 1
        if fall[z] == "x":
            if z != 0:
                if fall[z-1] == "-":
                    currefra *= -1
                    currnedra *= -1
                elif fall[z-1].isnumeric():
                    margfeldi *= int(fall[z-1])
                    if z >= 2:
                        if fall[z-2] == "-":
                            currefra *= -1
                            currnedra *= -1
            if z != len(fall)-1:
                if fall[z+1].isnumeric():
                    currefra = currefra**(int(fall[z+1])+1)
                    currefra *= margfeldi
                    currefra = (1/(int(fall[z+1])+1))*currefra
                    #neðra
                    currnedra = currnedra**(int(fall[z+1])+1)
                    currnedra *= margfeldi
                    currnedra = (1/(int(fall[z+1])+1))*currnedra
            else:
                currefra = currefra**2
                currefra = (1/2)*margfeldi*currefra
                #nedra
                currnedra = currnedra**2
                currnedra = (1/2)*margfeldi*currnedra
        elif fall[z].isnumeric():
            currefra = int(emork)*int(fall[z])
            currnedra = int(nmork)*int(fall[z])
            if z != 0:
                if fall[z-1] == "x":
                    currefra = 0
                    currnedra = 0
                elif fall[z-1] == "-":
                    currefra *= -1
                    currnedra *= -1
            if z != len(fall)-1:
                if fall[z+1] == "x":
                    currefra = 0
                    currnedra = 0
        efrisumma = currefra
        nedrisumma = currnedra
        totalsumma = abs(efrisumma-(nedrisumma))
    return totalsumma
print("fyrsta fall:")
print(heildun(emork,nmork,fall1))
print("Seinna fall:")
print(heildun(emork,nmork,fall2))
if heildun(emork,nmork,fall1) > heildun(emork,nmork,fall2):
    print("samanlagt:",heildun(emork,nmork,fall1)-heildun(emork,nmork,fall2))
else:
    print("samanlagt:",heildun(emork,nmork,fall1)-heildun(emork,nmork,fall2))

#Euler vandamál from top to bottom
with open('triangle.txt','r') as file:
    innihald = file.read().split('\n')

for x in range(len(innihald)):
    innihald[x] = innihald[x].split(" ")
    innihald[x] = list(map(int,innihald[x]))
#print(innihald)
print(innihald[99])
def maxsum(listi,lina,index,summa):
    trihyrn = listi
    lina = lina
    index = index
    summa = summa
    if lina == 99:
        print(trihyrn[lina][0])
        return summa
    if lina == 0 and summa == 0:
        summa += trihyrn[0][0]
        print("default winner: ",trihyrn[0][0])
        print(summa)
        return maxsum(trihyrn,lina,index,summa)
    else:
        if trihyrn[lina+1][index] > trihyrn[lina+1][index+1]:
            print(trihyrn[lina+1][index],'vs',trihyrn[lina+1][index+1])
            print('winner:',trihyrn[lina+1][index])
            print("lina:",lina+1)
            summa = summa+trihyrn[lina+1][index]
            print("summa:",summa)
            return maxsum(trihyrn,lina+1,index,summa)
        else:
            print(trihyrn[lina+1][index+1],'vs',trihyrn[lina+1][index])
            print('winner:',trihyrn[lina+1][index+1])
            print("lina:",lina)
            summa = summa+trihyrn[lina+1][index+1]
            print("summa:",summa)
            return maxsum(trihyrn,lina+1,index+1,summa)
print(maxsum(innihald,0,0,0))


#binary search tree
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def preOrder(self):
        if self:
            print(self.value)
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def postOrder(self):
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(self.value)

    def delete(self,n):
        if self.value > n:
            self.left = self.left.delete(n)
        elif self.value < n:
            self.right = self.right.delete(n)
        else:
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp
        return self

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):
        if self.root:
            self.root.preOrder()
        else:
            return self.root

    def postOrderPrint(self):
        if self.root:
            self.root.postOrder()
        else:
            return self.root

    def delete(self,n):
        if self.root:
            return self.root.delete(n)
        else:
            return False

    def deleteTree(self):
        if self.root:
            self.root = None
            return True
        else:
            return False
t = Tree()
t.insert(5)
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(4)
t.insert(9)
print("pre order print:")
t.preOrderPrint()
print("post order print:")
t.postOrderPrint()
print("delete")
t.delete(9)
t.preOrderPrint()
