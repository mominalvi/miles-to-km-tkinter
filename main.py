from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.focus()
miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)
num_km = Label(text=0)
num_km.grid(column=1, row=1)
km = Label(text="Km")
km.grid(column=3, row=1)

def button_clicked():
    user_input = float(entry.get())
    num_km.config(text=user_input*1.6)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)



window.mainloop()
