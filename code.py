#Fannar Hrafn Haraldsson
#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
#heildun og flatarmál
import math
fall=input("sláðu inn fall f(x): ")
emork=input("sláðu inn x fyrir efri mörk: ")
nmork=input("sláðu inn y fyrir neðri mörk: ")
efrisumma = 0
nedrisumma = 0
for z in range(len(fall)):
    currefra = 0
    currnedra = 0
    margfeldi = 1
    if fall[z] == "x":
        currefra += int(emork)
        currnedra += int(nmork)
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
    print("z:",z)
    print("curre:",currefra)
    print("currn:",currnedra)
    efrisumma += currefra
    nedrisumma += currnedra
print(efrisumma," + ",nedrisumma)
totalsumma = abs(efrisumma-(nedrisumma))
print("=",totalsumma)
'''
with open('triangle.txt','r') as file:
    innihald = file.read().split('\n')
    del innihald[-1]

for x in range(len(innihald)):
    innihald[x] = innihald[x].split(" ")
    innihald[x] = list(map(int,innihald[x]))
#print(innihald)
#print(innihald[67][3]+1)
def maxsum(listi,lina,index,summa):
    trihyrn = listi
    lina = lina
    index = index
    summa = summa
    if lina == 0 and summa == 0:
        summa += trihyrn[0][0]
        print("default winner: ",trihyrn[0][0])
        print(summa)
        return maxsum(trihyrn,lina,index,summa)
    elif lina == 99:
        return summa
    else:
        if trihyrn[lina+1][index] > trihyrn[lina+1][index+1]:
            print(trihyrn[lina+1][index],'vs',trihyrn[lina+1][index+1])
            print('winner:',trihyrn[lina+1][index])
            print("lina:",lina+1)
            summa = summa+trihyrn[lina+1][index]
            print("summa:",summa)
            return maxsum(trihyrn,lina+1,index,summa)
        elif trihyrn[lina+1][index] == trihyrn[lina+1][index+1]:
            print("eins tölur í línu",lina,trihyrn[lina+1][index],"vs",trihyrn[lina+1][index+1])
        else:
            print(trihyrn[lina+1][index+1],'vs',trihyrn[lina+1][index])
            print('winner:',trihyrn[lina+1][index+1])
            print("lina:",lina)
            summa = summa+trihyrn[lina+1][index+1]
            print("summa:",summa)
            return maxsum(trihyrn,lina+1,index+1,summa)
print(maxsum(innihald,0,0,0))

