from tkinter import *
import API
import FilmFrame

def beginscherm(id):

    window = Tk()

    textLabel=Label(master=window, background="Green", width=50, height=40)
    textLabel.pack(side=LEFT)

    def klik_vandaag():

        dictionary = API.ophalenFilms("Vandaag")

        films = dictionary['filmsoptv']['film']
        y = 50
        labels = []
        for film in films:

            labels.append(Label(master=window, text=film['titel']))

        for label in labels:

            label.place(x=30, y=y)
            label.bind("<Button-1>", lambda e, film = label.cget("text"): openFilm(film, "Vandaag"))

            y += 20

    def klik_morgen():

        dictionary = API.ophalenFilms("Morgen")

        films = dictionary['filmsoptv']['film']
        y = 50
        labels = []
        for film in films:

            labels.append(Label(master=window, text=film['titel']))

        for label in labels:

            label.place(x=210, y=y)
            label.bind("<Button-1>", lambda e, film = label.cget("text"): openFilm(film,"Morgen"))

            y += 20

    def openFilm(titel,dag):
        FilmFrame.run(titel, dag, id)


    knop_vandaag = Button(window, text="Vandaag", command=klik_vandaag)
    knop_vandaag.place(x=10, y=10)

    knop_morgen = Button(window, text="Morgen", command=klik_morgen)
    knop_morgen.place(x=200, y=10)





    window.mainloop()