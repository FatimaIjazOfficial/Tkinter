from tkinter import *


def formula():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


windows = Tk()
windows.title("Mile to Km Converter")
windows.config(padx=100, pady=50,background="Green")

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles",background="Green")
miles_label.grid(column=2, row=0)

is_equal_input = Label(text="is equal to",background="Green")
is_equal_input.grid(column=0, row=1)

kilometer_result_label = Label(text="0",width=12,background="Orange")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate",command=formula,background="Purple")
calculate_button.grid(column=1, row=2)




windows.mainloop()
