import os
import model
# zacetni uvoz

def niz_v_fingerprint(name):
    name=name.replace(" ", "")
    print(name)

    fingerprint = []
    name = name[1:-5]
    y = name.split("','")
    for x in y:
        y = x.split(",")
        fingerprint.append([int(j) for j in x.split(",") if j])
    return fingerprint

orozarna = model.Orozarna()
for root, dirs, files in os.walk(r"C:\Users\laram\OneDrive\Namizje\Lara\UVP\orožarna\Slike", topdown=False):
   uid = 0
   for name in files:
        fp = (niz_v_fingerprint(name))

        orozarna.dodaj_sopek(fp)

orozarna.shrani_v_json_datoteko(ime_datoteke="podatki.json")

