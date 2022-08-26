from tkinter import *

#from click import *
import time
from tokenize import Number
import keyboard
import pyautogui as pa
import random



def aceptGame():
    num = seg.get()
    duration = float(num)
    
    while(duration>0):
        #duration = int(seg.get())
        pa.moveTo(x=960, y=674)
        pa.click()
        duration-=5
        time.sleep(5)
    return print ("Programa finalizado.")




window = Tk()
window.title("Programa")
window.geometry("400x200")

lbl = Label(window, text="Programa")
lbl.pack()

seg = Entry(window, bg="#ccc")
seg.place(x=10, y=10, width=100, height=30)

btn = Button(window, text="Iniciar", command= aceptGame)
btn.pack()

window.mainloop()
