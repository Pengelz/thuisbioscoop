from tkinter import *
import csv

def show(code, id,titel):
    window = Tk()
    label = Label(master=window, text=code).pack()
    save(code,id, titel)
    window.mainloop()
def save(code,id,titel):
    file = open('database/gekocht.csv', 'a', newline='')
    write = csv.writer(file)
    write.writerow((id, code, titel))
    file.close()
    return None
