from tkinter import *
import API
import FilmFrame

def beginscherm(id):

    window = Tk()

    textLabel=Label(master=window, background="Green", width=80, height=40)
    textLabel.pack(side=LEFT)

    def klik_vandaag():

        dictionary = API.ophalenFilms("Vandaag")

        films = dictionary['filmsoptv']['film']
        y = 50
        titelLabels = []
        aanbiederLabels = []

        for film in films:

            titelLabels.append(Label(master=window, text=film['titel']))
            aanbiederLabels.append(Label(master=window, text=film['zender']))

        for label in titelLabels:

            label.place(x=50, y=y)
            label.bind("<Button-1>", lambda e, film = label.cget("text"): openFilm(film, "Vandaag"))

            y += 20

        y = 50
        for label in aanbiederLabels:

            label.place(x=200, y=y)

            y+=20

    def klik_morgen():

        dictionary = API.ophalenFilms("Morgen")

        films = dictionary['filmsoptv']['film']
        y = 50

        filmLabels = []
        aanbiederLabels = []

        for film in films:

            filmLabels.append(Label(master=window, text=film['titel']))
            aanbiederLabels.append(Label(master=window, text=film['zender']))

        for label in filmLabels:

            label.place(x=300, y=y)
            label.bind("<Button-1>", lambda e, film = label.cget("text"): openFilm(film,"Morgen"))

            y += 20

        y = 50

        for label in aanbiederLabels:

            label.place(x=500, y=y)

            y += 20

    def openFilm(titel,dag):
        FilmFrame.run(titel, dag, id)


    knop_vandaag = Button(window, text="Vandaag", command=klik_vandaag)
    knop_vandaag.place(x=50, y=10)

    knop_morgen = Button(window, text="Morgen", command=klik_morgen)
    knop_morgen.place(x=300, y=10)





    window.mainloop()