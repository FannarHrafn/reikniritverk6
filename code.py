#Fannar Hrafn Haraldsson
#heildun
import math
fall=input("sláðu inn fall f(x): ")
emork=input("sláðu inn x fyrir efri mörk: ")
nmork=input("sláðu inn y fyrir neðri mörk: ")
efrisumma = 0
nedrisumma = 0
for z in range(len(fall)):
    curr = 0
    if fall[z] == "x":
        curr += int(emork)
        if z != 0:
            if fall[z-1] == "-":
                curr *= -1
            elif fall[z-1].isnumeric():
                curr *= int(fall[z-1])
            if z >= 3:
                if fall[z-2] == "-":
                    curr *= -1
        print("extra curr:",curr)
        if z != len(fall)-1:
            if fall[z+1].isnumeric():
                curr = curr**(int(fall[z+1])+1)
                curr = (1/(int(fall[z+1])+1))*curr
            else:
                curr = curr**2
                curr = (1/2)*curr
    elif fall[z].isnumeric():
        curr = int(emork)*int(fall[z])
        if z != 0:
            if fall[z-1] == "x":
                curr = 0
            elif fall[z-1] == "-":
                curr *= -1
        if z != len(fall)-1:
            if fall[z+1] == "x":
                curr = 0
    print("z:",z)
    print("curr:",curr)
    efrisumma += curr
print(efrisumma)
'''
for z in range(len(fall)):
    curr = 0
    if fall[z] == "x":
        curr += int(nmork)
        if z != 0:
            if fall[z-1] == "-":
                curr *= -1
            elif fall[z-1].isnumeric():
                curr *= fall[z-1]
            if z >= 3:
                if fall[z-2] == "-":
                    curr *= -1
        if z != len(fall)-1:
            if fall[z+1].isnumeric():
                curr = (1/int(fall[z+1])+1)*curr**int(fall[z+1])+1
    if fall[z].isnumeric():
        curr = int(nmork)*int(fall[z])
        if z != 0:
            if fall[z-1] == "x":
                curr = 0
            elif fall[z-1] == "-":
                curr *= -1
        if z != len(fall)-1:
            if fall[z+1] == "x":
                curr = 0
    nedrisumma +=curr

totalsumma = efrisumma-(nedrisumma)
print(totalsumma)
'''
