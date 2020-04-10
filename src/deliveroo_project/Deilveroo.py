import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")

headline_text = tk.Label(text="Meals without a Deliveroo!!")
headline_text.grid(column=2, row=0)

deliveroo_button = tk.Button (window, text="Deliveroo")
deliveroo_button.grid(column=0,row=4)

deliveroo_button = tk.Button (window, text="Not Deliveroo")
deliveroo_button.grid(column=3,row=4)

days_count = tk.Label(text=0)
days_count.grid(column=2,row=1)

window.mainloop()