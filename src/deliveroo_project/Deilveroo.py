import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")

headline_text = tk.Label(text="Meals without a Deliveroo!! test")
headline_text.grid(column=0, row=0)


days_count = tk.Label(text=0)
days_count.grid(column=0,row=1)

window.mainloop()