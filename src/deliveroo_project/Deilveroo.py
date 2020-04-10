import tkinter as tk
from tkinter import *

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        headline_text = tk.Label(self, text="Meals without a Deliveroo!!", font=("Ariel",144), fg="red")
        #headline_text.grid(column=2, row=0)
        headline_text.pack()

        self.label_var = tk.IntVar()
        label = tk.Label(self, textvariable=self.label_var, font=("Ariel",300), fg="red")  # Assigned that  variable to the label
        label.pack()
        #label.grid(column=2,row=1)

        deliveroo_button = tk.Button(self, text="Deliveroo",
                                     relief="groove", command=self.reset_var, width=30, height=5)
        #deliveroo_button.grid(column=0, row=4)
        deliveroo_button.pack(side=LEFT)

        not_deliveroo = tk.Button(self, text="Not Deliveroo!!",
                           relief="groove", command=self.add_var, width=30, height=5)
        #not_deliveroo.grid(column=3, row=4)
        not_deliveroo.pack(side=RIGHT)

    def add_var(self):
        self.label_var.set(self.label_var.get() + 1)

    def reset_var(self):
        self.label_var.set(0)

root = tk.Tk()
root.title("Meals Without Deliveroo!!")
root.resizable()
root.geometry("2500x1000")
game = Game(root)
game.pack()
root.mainloop()