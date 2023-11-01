import os

import hashlib
import re

def hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        digest = hashlib.sha256(bytes).hexdigest()
    return digest

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
longestFiles = []
for fil in files:
    cant = cumplen(fil, f1)
    if cant > m:
        m = cant
        longestFiles = [fil]
    elif cant == m:
        longestFiles.append(fil)

if len(longestFiles) > 0:
    print(longestFiles[0])
else:
    print("No hay ficheros que cumplan las condiciones")
