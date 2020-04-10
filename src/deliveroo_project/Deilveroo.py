import tkinter as tk
from tkinter import *

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        headline_text = tk.Label(self, text="Meals Without Deliveroo!!", font=("Ariel",160), fg="red")
        headline_text.pack()

        self.label_var = tk.IntVar()
        label = tk.Label(self, textvariable=self.label_var, font=("Ariel",600), fg="black")  # Assigned that  variable to the label
        label.pack()

        deliveroo_button = tk.Button(self, text="Deliveroo",
                                     relief="groove", command=self.reset_var, width=20, height=20, font=("Ariel",70), fg="red")
        deliveroo_button.pack(side=LEFT)

        not_deliveroo = tk.Button(self, text="Not Deliveroo!!",
                           relief="groove", command=self.add_var, width=20, height=20, font=("Ariel",70), fg="green")
        not_deliveroo.pack(side=RIGHT)

    def add_var(self):
        self.label_var.set(self.label_var.get() + 1)

    def reset_var(self):
        self.label_var.set(0)

root = tk.Tk()
root.title("Meals Without Deliveroo!!")
root.attributes('-fullscreen', True)
#root.resizable()
#root.geometry("2500x1000")
game = Game(root)
game.pack()
root.mainloop()