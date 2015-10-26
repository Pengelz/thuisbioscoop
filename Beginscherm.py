from tkinter import *
import API
from tkinter.messagebox import showinfo

window = Tk()

textLabel=Label(master=window, background="Green", width=50, height=40)
textLabel.pack(side=LEFT)

def klik_vandaag():
    dictionary = API.ophalenFilms("Vandaag")

    films = dictionary['filmsoptv']['film']
    y=50
    for film in films:
        vandaagLabel = Label(master=window, text=film['titel'])
        vandaagLabel.place(x=30, y=y)
        y+=20

def klik_morgen():
    dictionary = API.ophalenFilms("Morgen")

    films = dictionary['filmsoptv']['film']
    y=50
    for film in films:
        vandaagLabel = Label(master=window, text=film['titel'])
        vandaagLabel.place(x=210, y=y)
        y+=20

knop_vandaag = Button(window, text="Vandaag", command=klik_vandaag)
knop_vandaag.place(x=10, y=10)

knop_morgen = Button(window, text="Morgen", command=klik_morgen)
knop_morgen.place(x=200, y=10)





window.mainloop()