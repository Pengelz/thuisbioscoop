from tkinter import *
from csv import DictReader
from collections import OrderedDict
import API

def adminscherm(id):

    window = Tk()


    def getUsername(id):
        username = ""
        with open('database/users.csv') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if row['id'] == id:
                    username = row['username']
            return username

    def getInfo(username):
        info = []
        with open('database/gekocht.csv') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if row['aanbieder'] == username:
                    row['username'] = getUsername(row['id'])
                    info.append(row)
            return info



    username = getUsername(id)
    info = getInfo(username)
    sorted_info = sorted(info, key= lambda aankoop: aankoop['starttijd'])

    y = 10
    sorted_titels = []
    for aankoop in sorted_info:
        if aankoop['titel'] not in sorted_titels:
            sorted_titels.append(aankoop['titel'])
            titelLabel = Label(master=window, text=aankoop['titel'])
            titelLabel.place(x=10,y=y)
            bezoekers = []
            for aankoop2 in info:
                if aankoop2['titel'] == aankoop['titel']:
                    bezoekers.append(aankoop2['username'])
            sorted_bezoekers = sorted(bezoekers)
            for bezoeker in sorted_bezoekers:
                bezoekerLabel = Label(master=window, text=bezoeker)
                bezoekerLabel.place(x = 110, y=y)
                y +=20
                
    window.mainloop()