import bottle
import os
import model
from model import Sopek
import json


@bottle.get("/")
def osnovna_stran():
    stanje = izbira()
    return bottle.template(
        "osnovna_stran.html",
        namen=stanje.namen(),
        tip=stanje.tip(),
        barva=stanje.barva(),
        roze=stanje.roze(),
        uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"),
    )


@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
    bottle.redirect("/")


@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    print("piškotek uspešno pobrisan")
    bottle.redirect("/")


@bottle.post("/izberi/")
def izberi_svoj_sanjski_aranžma():
    namen = bottle.request.forms.getunicode("namen")
    tip = bottle.request.forms.getunicode("tip")
    barva = bottle.request.forms.getunicode("barva")
    roza = bottle.request.forms.getunicode("roza")   
    print(namen)
    izbira = Sopek(namen, tip, barva,roza)
    stanje = izbira()
    stanje.dodaj_izbiro(izbira)
    shrani_izbiro(izbira)
    bottle.redirect("/")




@bottle.post("/pokazi izbrano/")
def pokazi_izbrano():
    indeks = bottle.request.forms.getunicode("indeks")
    stanje = izberi_svoj_sanjski_aranžma()
    bottle.redirect("/https://drive.google.com/drive/folders/17m8-n03kBdhueTJ6-yuDrOv9hwd1rw47?usp=sharing")




@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)