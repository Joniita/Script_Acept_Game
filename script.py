from tkinter import *

import time
from tokenize import Number
from turtle import position
import keyboard
import pyautogui as pa
import random

def conv():
    num = seg.get()
    duration = float(num)
    #duration +=1
    aceptGame(duration)

def aceptGame(duration):
    
    
    while(duration>0):
        #duration = int(seg.get())
        #seg.delete("0", "end")
        
        print("Ejecutando...")
        #duration-=1
        time.sleep(5)
        pa.moveTo(x=960, y=674)
        pa.click()
        break
        
       
        
    return print ("Programa finalizado.")
    

    

    
    #while(duration>0):
     #   pa.moveTo(x=960, y=674)
        #pa.click()
        #duration-=5
      #  duration-=1
       # time.sleep(5)
        #pa.click()
    #return print ("Programa ejecutandose.")




window = Tk()
window.title("Programa")
window.geometry("400x200"+"+760"+"+605")

lbl = Label(window, text="Programa")
lbl.pack()

seg = Entry(window, bg="#ccc")
seg.place(x=10, y=10, width=100, height=30)

btn = Button(window, text="Iniciar", command= conv)
btn.pack()

window.mainloop()
