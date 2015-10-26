from tkinter import *
from tkinter.messagebox import showinfo

window = Tk()

textLabel=Label(master=window, background="Green", width=50, height=40)
textLabel.pack(side=LEFT)

def klik_vandaag():
    vandaagLabel = Label(master=window, text="Film 1\n\n\nFilm 2\n\n\nFilm 3\n\n\nFilm 4\n\n\nFilm 5", background="Green")
    vandaagLabel.place(x=30, y=50)

def klik_morgen():
    morgenLabel = Label(master=window, text="Film 1\n\n\nFilm 2\n\n\nFilm 3\n\n\nFilm 4\n\n\nFilm 5", background="Green")
    morgenLabel.place(x=265, y=50)

knop_vandaag = Button(window, text="Vandaag", command=klik_vandaag)
knop_vandaag.place(x=10, y=10)

knop_morgen = Button(window, text="Morgen", command=klik_morgen)
knop_morgen.place(x=200, y=10)





window.mainloop()