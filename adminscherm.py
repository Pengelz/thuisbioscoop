from tkinter import *
from csv import DictReader
import datetime

def adminscherm(id):

    window = Tk()
    window.geometry('500x200')


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

    def showInfo(sorted_info):
        y = 10
        sorted_titels = []
        sorted_time = []
        for aankoop in sorted_info:
            if aankoop['titel'] not in sorted_titels and aankoop['starttijd'] not in sorted_time:
                sorted_titels.append(aankoop['titel'])
                sorted_time.append(aankoop['starttijd'])
                titelLabel = Label(master=window, text=aankoop['titel'])
                titelLabel.place(x=10,y=y)
                timeLabel = Label(master=window, text=datetime.datetime.fromtimestamp(int(aankoop['starttijd'])).strftime("%H:%M    %d-%m-%Y"))
                timeLabel.place(x=100, y=y)
                bezoekers = []
                for aankoop2 in info:
                    if aankoop2['titel'] == aankoop['titel'] and aankoop2['starttijd'] == aankoop['starttijd']:
                        bezoekers.append(aankoop2['username'])
                sorted_bezoekers = sorted(bezoekers)
                for bezoeker in sorted_bezoekers:
                    bezoekerLabel = Label(master=window, text=bezoeker)
                    bezoekerLabel.place(x=210, y=y)
                    y+=20

    username = getUsername(id)
    info = getInfo(username)
    sorted_info = sorted(info, key= lambda aankoop: aankoop['starttijd'])
    showInfo(sorted_info)

    window.mainloop()