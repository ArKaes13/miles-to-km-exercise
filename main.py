from tkinter import *


def button_clicked():
    conversion = round(float(miles_entry.get()) * 1.609344, 1)
    label_3.config(text=conversion)


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

label_1 = Label(text='Miles', font=('Arial', 12, 'bold'))
label_1.grid(column=2, row=0)

label_2 = Label(text='is equal to', font=('Arial', 12, 'bold'))
label_2.grid(column=0, row=1)

label_3 = Label(text='', font=('Arial', 12, 'bold'))
label_3.grid(column=1, row=1)

label_4 = Label(text='Km', font=('Arial', 12, 'bold'))
label_4.grid(column=2, row=1)

button = Button(text='Calculate', font=('Arial', 12, 'bold'), command=button_clicked)
button.grid(column=1, row=2)

miles_entry = Entry(width=12)
miles_entry.grid(column=1, row=0)


window.mainloop()
