import os

import hashlib
import re
import random

def hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        digest = hashlib.sha256(bytes).hexdigest()
    return digest

def sorteoPonderado(longestFiles):
    den = 0
    for k in longestFiles.keys():
        den += k*len(longestFiles[k])
    r = random.random()

    cu = 0
    for ke in longestFiles.keys():
        if r > (ke*len(longestFiles[ke])+cu)/den:
            cu += ke*len(longestFiles[ke])
        else:
            for i in range(len(longestFiles[ke])):
                if r > (ke+cu)/den:
                    cu += ke
                else:
                    return longestFiles[ke][i]
                
def cumplen(filename1, filename2):
    with open(filename1,"r") as f:
        len1 = len(f.readlines())

    with open("../"+filename2, "r") as f:
        len2 = len(f.readlines())

    if abs(len1-len2) != 1:
        return -1

    else:
        if len2 > len1:
            ff = filename1
            filename1 = filename2
            filename2 = ff

            ll = len1
            len1 = len2
            len2 = ll
        
        same = True
        with open(filename1, "r") as f1:
            with open("../"+filename2, "r") as f2:
                for line2 in f2:
                    af = f1.readline()
                    if line2 != af and af != line2+"\n":
                        same = False
                        return -1
                
                h = hash(filename1)
                if same and h[0] == "0" and re.search("[0-9a-z]{8}\t[0-9a-z]{2}\t100", f1.readline()):
                    for i in range(1,len(h)):
                        if h[i] != "0":
                            return i
                else:
                    return -1

f1 = input("Escribe el nombre del fichero: ")
d1 = input("Escribe el nombre del directorio: ")

os.chdir(d1)
files = os.listdir()
m = 0
longestFiles = {}
for fil in files:
    cant = cumplen(fil, f1)
    if cant > 0:
        if cant not in longestFiles.keys():
             longestFiles[cant] = [fil]
        else:
            longestFiles[cant].append(fil)

if len(longestFiles.keys()) > 0:
    print(sorteoPonderado(longestFiles))
else:
    print("No hay ficheros que cumplan las condiciones")
