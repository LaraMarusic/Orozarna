import os
import model

'1'.split(",")

def niz_v_fingerprint(name):
    print(name)
    name=name.replace(" ", "")
    fingerprint = []
    name = name[1:-5]
    y = name.split("','")
    for x in y:
        y = x.split(",")
        fingerprint.append([int(j) for j in x.split(",")])
    return fingerprint


for root, dirs, files in os.walk(r"C:\Users\laram\OneDrive\Namizje\Lara\UVP\orožarna\Slike", topdown=False):
   uid = 0
   for name in files:
        fp = (niz_v_fingerprint(name))
        sopek = model.Sopek(uid,fp)
        uid += 1

