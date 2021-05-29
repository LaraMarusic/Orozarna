import json
from json import encoder

namen = 'n'
tip = 't'
barva = 'b'
rože = 'r'

class Sopek:
    """Izberemo kakšen aranžma želimo in nato poiščemo sliko, ki mu je vektorsko najbližje  """

    def __init__(self, uid, fp):
        self.uid = uid
        self.fp = fp

    def izbira(self,izbira):
        self.izbira = izbira[:]

    def vektor(self,vektor):
        self.vektor = vektor[:]

    def id(fp):
        uid = 0
        for x in fp:
            if x == fp:
                pass
            else:
                uid += 1

    

    
    def primerjava_fingerprint_izbira(fp, izbira):
        primerjava_namen = izbira & fp[1] 
        primerjava_tip = izbira & fp[2]
        primerjava_barva = izbira & fp[3]
        primerjava_roze = izbira & fp[4]
        return [primerjava_namen, primerjava_tip, primerjava_barva, primerjava_roze]

    def najboljsi_kompromisi(izbira):
        stevilo_izbire = {}
        for x in izbira:
            for namen,tip,barva,roze in izbira:
                stevilo_izbire[namen] = stevilo_izbire.get(namen, 0) + 1
                stevilo_izbire[tip] = stevilo_izbire.get(tip, 0) + 1
                stevilo_izbire[barva] = stevilo_izbire.get(barva, 0) + 1
                stevilo_izbire[roze] = stevilo_izbire.get(roze, 0) + 1
        max_ujemanje = 0
        naj_priblizek = set()

        for izbira in stevilo_izbire:    
            if stevilo_izbire[izbira] > max_ujemanje:
                naj_priblizek = {izbira}
                max_ujemanje = stevilo_izbire[izbira]
            elif stevilo_izbire[izbira] == max_ujemanje:
                naj_priblizek.add(izbira)

        return naj_priblizek


    def dobi_json_slovar(self):
        return {
            "fp": self.fp,
        }



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

    

    

    





