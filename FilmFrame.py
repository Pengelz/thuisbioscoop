from tkinter import *
import API
import kaartje

def run(titel,dag,id):
    window = Tk()
    film = API.ophalenInfo(titel,dag)
    kopen = Button(window, text="Kaartje kopen", command=lambda :showKaartje(titel,id, film['zender'],film['starttijd']))
    kopen.place(x=10, y=10)
    window.mainloop()

def showKaartje(titel,id, aanbieder, starttijd):
    kaartje.show(koop(titel,id), id, titel, aanbieder, starttijd)

def koop(titel, id):
    invoer = titel + id
    enc2 = ""
    for i in invoer:
        enc = ord(i) + 3
        enc2 = enc2 + chr(enc)
    return enc2
