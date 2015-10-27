from csv import DictReader
from tkinter import *
import tkinter.messagebox as tm
import Beginscherm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.username = ""
        self.id = ""

        self.label_1 = Label(self, text="Gebruiker")
        self.label_2 = Label(self, text="Wachtwoord")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.loginbtn = Button(self, text="Login", command=self._login_btn_clicked)

        self.showLogin()

        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()

        if self.login(username, password):
            tm.showinfo("Login info", "Welkom " + str(self.username))
            root.destroy()
            Beginscherm.beginscherm(self.id)

        else:
            tm.showerror("Login error", "Incorrecte gebruikersnaam/wachtwoord")

    def login(self, username, password):
        with open('database/users.csv') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    self.username = row["username"]
                    self.id = row["id"]
                    return True

            return False

    def showLogin(self):
        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=1, column=0)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.loginbtn.grid(row=2, column=1)

root = Tk()
loginFrame = LoginFrame(root)
root.resizable(width=FALSE, height=FALSE)
root.geometry("800x600")
root.mainloop()
