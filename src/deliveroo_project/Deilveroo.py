import tkinter as tk
from tkinter import *

#def incrementNotDeliverooCounter():


counter = 0

def incrementNotDeliveroo():
    return

def resetCounter():
    return


window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")

headline_text = tk.Label(text="Meals without a Deliveroo!!")
headline_text.grid(column=2, row=0)

deliveroo_button = tk.Button (window, text="Deliveroo", command=resetCounter)
deliveroo_button.grid(column=0,row=4)

deliveroo_button = tk.Button (window, text="Not Deliveroo", command=incrementNotDeliveroo)
deliveroo_button.grid(column=3,row=4)

days_count = tk.Label(text=counter)
days_count.grid(column=2,row=1)

window.mainloop()