#Fannar Hrafn Haraldsson
#heildun
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
