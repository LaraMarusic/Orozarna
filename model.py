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
    
    def dobi_json_slovar(self):
        slovar_sopkov = {}
        for uid in self.sopek.items():
            slovar_sopkov[uid] = [
                fp.dobi_json_slovar(),uid
            ]
        return {
            "sopek": slovar_sopkov,
            "os" : self.os.py
            }

