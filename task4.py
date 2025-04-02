import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("320x130")
window.attributes("-topmost", True)
window.title("Example")
window.resizable(False,False)
window.configure(bg="#fff")
nF= Frame()

dogphoto = PhotoImage(file="dog.png")
label0 = tk.Label(nF, image=dogphoto, borderwidth=0)
Label1 = Label(nF,text="Pochacco!", bg="#fff")
Label2 = Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#54E0DA", width=45)



nF.pack()

label0.pack(side = LEFT)
Label1.pack(side =LEFT)

Label2.pack()

window.mainloop()