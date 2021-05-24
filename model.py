import json
from json import encoder

namen = 'n'
tip = 't'
barva = 'b'
rože = 'r'

class Sopek:

    def __init__(self, uid, fp):
        self.uid = uid
        self.fp = fp

    def slika(self,slika):
        self.slika = slika[:]

    def vektor(self,vektor):
        self.vektor = vektor[:]

    def id(fp):
        uid = 0
        for x in fp:
            if x == fp:
                pass
            else:
                uid += 1

    
    

    def namen(n,fp):
        a = 0
        for x in fp:
            if x == fp:
                a += 1
                return a
            else:
                pass
        return a

    def tip(t,fp):
        b = 0
        for x in fp:
            if x == fp:
                b += 1
                return b
            else:
                pass
        return b

    def barva(b,fp):
        c = 0
        for x in fp:
            if x == fp:
                c += 1
                return c
            else:
                pass
        return c

    def rože(r,fp):
        d = 0
        for x in fp:
            if x == fp:
                d += 1
                return d
            else:
                pass
        return d

    def seštej(a,b,c,d):
        s = sum(a,b,c,d)
        return s

    def naj_rezultat(s,uid):
        max





    def dobi_json_slovar(self):
        return {
            "fp": self.fp,
        }




            
#      Link : https://drive.google.com/drive/folders/17m8-n03kBdhueTJ6-yuDrOv9hwd1rw47?usp=sharing

class Orozarna:

    def __init__(self, zacetni_sopki = None , prost_id = 0):
        self.sopki = zacetni_sopki = {}
        self.prost_id = prost_id
        

    def json_slovar(self):
        slovar = {}
        for uid, sopek in self.sopki.items():
            slovar[uid] = sopek.dobi_json_slovar()
        return slovar

    def shrani_v_json_datoteko(self, ime_datoteke):
        with open(ime_datoteke, 'w') as out_file:
            json.dump(self.json_slovar(), out_file, indent=None)


    def nov_id(self):
        self.prost_id += 1
        return self.prost_id
        
    def dodaj_sopek(self, fp):
        uid = self.nov_id()
        sopek = Sopek(uid,fp)
        self.sopki[uid] = sopek

    @staticmethod
    def prevedi_json(json_slovar):
        slovar_sopek = {}
        for uid, sopek_slovar in json_slovar.items():
            slovar_sopek[int(uid)] = [
                Sopek.prevedi_json(sopek_slovar)
            ]

        return Orozarna(
            slovar_sopek, max(slovar_sopek.keys()) + 1
        )

    

    

    





