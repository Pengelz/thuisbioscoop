from tkinter import *
import API
import kaartje
from urllib.request import urlopen
import io
from PIL import Image, ImageTk
import Beginscherm

def run(titel,dag,id):
    window = Tk()

    def showKaartje(titel,id, aanbieder, starttijd):
        window.destroy()
        kaartje.show(koop(titel,id), id, titel, aanbieder, starttijd)

    def back(id):
        window.destroy()
        Beginscherm.beginscherm(id)

    def koop(titel, id):
        invoer = titel + id
        enc2 = ""
        for i in invoer:
            enc = ord(i) + 3
            enc2 = enc2 + chr(enc)
        return enc2

    film = API.ophalenInfo(titel,dag)
    kopen = Button(window, text="Kaartje kopen", command=lambda :showKaartje(titel,id, film['zender'],film['starttijd']))
    kopen.place(x=10, y=10)

    y = 140
    i = 0
    j = 30
    while i <= len(film['synopsis']):
        omschrijvinglabel = Label(master=window, text=film['synopsis'][i:j])
        omschrijvinglabel.place(x=10,y=y)
        i+=30
        j+=30
        y+=20


    titellabel = Label(master=window, text='Titel: '+film['titel'])
    jaarlabel = Label(master=window, text='Jaar: '+film['jaar'])
    regisseurlabel = Label(master=window, text='Regisseur: '+film['regisseur'])
    genrelabel = Label(master=window, text='Genre: ' +film['genre'])

    titellabel.place(x=10, y=50)
    jaarlabel.place(x=10,y=70)
    regisseurlabel.place(x=10,y=90)
    genrelabel.place(x=10,y=110)

    picurl=film['cover']
    pic_bytes = urlopen(picurl).read()
    data_stream = io.BytesIO(pic_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    photolabel=Label(image=tk_image)
    photolabel.place(x=210,y=30)
    window.geometry("800x600")
    window.mainloop()

