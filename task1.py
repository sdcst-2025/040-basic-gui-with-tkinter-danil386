import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("432x25")
window.attributes("-topmost", True)
window.resizable(False,False)

nF = Frame()

fentry1 = tk.Entry(nF,text="Entry widgets can be typed in", width=17)
flabel1 = tk.Label(nF,text="x")
fentry2 = tk.Entry(nF,text="Entry widgets can be typed in", width=17)
fbutton1 = tk.Button(nF,text="=", relief = FLAT)
fentry3 = tk.Entry(nF,text="Entry widgets can be typed in", width=31)


nF.pack()
fentry1.pack(side=LEFT)
flabel1.pack(side=LEFT)
fentry2.pack(side=LEFT)
fbutton1.pack(side=LEFT)
fentry3.pack(side=LEFT)



window.mainloop()