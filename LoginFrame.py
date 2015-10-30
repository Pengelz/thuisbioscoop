from csv import DictReader
import csv
from tkinter import *
import tkinter.messagebox as tm
import Beginscherm
import adminscherm
from collections import deque


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.username = ""
        self.id = ""
        self.type = ""

        self.label_0 = Label(self, text="Loginscherm")
        self.label_1 = Label(self, text="Gebruiker")
        self.label_2 = Label(self, text="Wachtwoord")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.loginbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.registerbtn = Button(self, text="Register", command=self._showRegister_btn_clicked)

        self.showLogin()

        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()

        if self.login(username, password) == "bezoeker":
            tm.showinfo("Login info", "Welkom " + str(self.username))
            root.destroy()
            Beginscherm.beginscherm(self.id)

        elif self.login(username, password) == "aanbieder":
            tm.showinfo("Login info", "Welkom " + str(self.username))
            root.destroy()
            adminscherm.adminscherm(self.id)

        else:
            tm.showerror("Login error", "Incorrecte gebruikersnaam/wachtwoord")

    def login(self, username, password):
        with open('database/users.csv') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if str(row["username"]) == username and row["password"] == password:
                    self.username = row["username"]
                    self.id = row["id"]
                    self.type = row["type"]
                    return self.type
            return False

    def _showRegister_btn_clicked(self):
        self.label_register = Label(self, text="Registreer gebruiker: ")
        self.label_register.grid(row=10)

        self.label_username = Label(self, text="Gebruiker ")
        self.label_username.grid(row=11, column=0)
        self.entry_username = Entry(self)
        self.entry_username.grid(row=11, column=1)

        self.label_password = Label(self, text="Wachtwoord ")
        self.label_password.grid(row=12, column=0)
        self.entry_password = Entry(self, show="*")
        self.entry_password.grid(row=12, column=1)

        self.label_email = Label(self, text="Email ")
        self.label_email.grid(row=13, column=0)
        self.entry_email = Entry(self)
        self.entry_email.grid(row=13, column=1)

        self.registreerbtn = Button(self, text="Register", command=self._registreer_btn_clicked)
        self.registreerbtn.grid(row=15, column=1)

    def getLastID(self):
        with open('database/users.csv', 'rt') as f:
            last_row = deque(csv.reader(f), 1)[0]
            return last_row[0]

    def _registreer_btn_clicked(self):
        self.reg_username = self.entry_username.get()
        self.reg_password = self.entry_password.get()
        self.reg_email = self.entry_email.get()
        self.reg_id = int(self.getLastID()) + 1
        file = open('database/users.csv', 'a', newline='')
        write = csv.writer(file)
        write.writerow((self.reg_id, self.reg_username, self.reg_password, self.reg_email, "bezoeker"))
        file.close()
        tm.showinfo('geregistreerd', 'U bent geregistreerd')



    def showLogin(self):
        self.label_0.grid(row=0)
        self.label_1.grid(row=1, column=0)
        self.label_2.grid(row=2, column=0)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)
        self.loginbtn.grid(row=3, column=1)
        self.registerbtn.grid(row=3, column=0)


root = Tk()
loginFrame = LoginFrame(root)
root.title("Filmtotaal Thuisbioscoop")
root.resizable(width=FALSE, height=FALSE)
root.geometry("600x600")
root.configure(bg='#9BA6C4')
root.mainloop()
