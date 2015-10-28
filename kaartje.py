from tkinter import *
import csv
import qrcode
from PIL import Image, ImageTk

def show(code, id, titel, aanbieder):
    window = Tk()
    label = Label(master=window, text=code).pack()
    save(code,id, titel, aanbieder)
    qr = qrcode.make(code)
    image = ImageTk.PhotoImage(qr)
    label2 = Label(image=image)
    label2.image=image
    label2.pack()
    window.mainloop()

def save(code,id,titel, aanbieder):
    file = open('database/gekocht.csv', 'a', newline='')
    write = csv.writer(file)
    write.writerow((id, code, titel, aanbieder))
    file.close()
    return None


