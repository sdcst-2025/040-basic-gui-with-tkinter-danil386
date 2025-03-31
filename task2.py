import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("570x180")
window.attributes("-topmost", True)
window.resizable(False,False)
window.configure(bg="#fff")

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto, borderwidth=0)

label2.grid(row = 1, column = 2, rowspan = 2)





window.mainloop()