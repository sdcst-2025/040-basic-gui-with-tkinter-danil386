import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("320x130")
window.attributes("-topmost", True)
window.title("Example")
window.resizable(False,False)
window.configure(bg="#fff")

dogphoto = PhotoImage(file="dog.png")
label0 = tk.Label(window, image=dogphoto, borderwidth=0)
Label1 = Label(window,text="Pochacco!", bg="#fff")
Label2 = Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#54E0DA", width=45)


label0.grid(row = 1, column = 2, rowspan = 3)
Label1.grid(row = 2, column = 3)
Label2.grid(row = 4, column = 1, columnspan = 4)


window.mainloop()