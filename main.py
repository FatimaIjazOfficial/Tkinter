from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Tkinter Usage")
window.minsize(1000, 600)
window.config(background="Black")

# Labels
label = Label(text="Label", font="Ariel", bg="Purple", border=20)
# label.config(text="Change Label",font="Ariel",bg="Purple",border=20)
label.pack()


# Buttons
def action():
    label.config(text="When I click the button ,so label change", font="Ariel", bg="Purple", border=20)


# calls action() when pressed
button = Button(text="Button", background="Pink", command=action, pady=10, padx=50)
button.pack()

# Entries
entry = Entry(width=50, border=30, background="Blue", font="Italic")
# Add some text to begin with
entry.insert(END, string="Entry")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=4, width=20)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Text")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# SpinBox

def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used, background="Yellow", font="Ariel")
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used, background="Red")
scale.pack()


# CheckButton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checkstate.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checkstate = IntVar()
checkbutton = Checkbutton(text="checkbutton", background="Grey", variable=checkstate, command=checkbutton_used)
checkstate.get()
checkbutton.pack()


# radioButton
def radiobutton_used():
    print(radiostate.get())


# Variable to hold on to which radio button value is checked.
radiostate = IntVar()
radiobutton1 = Radiobutton(text="RadioButton1", background="Orange", value=1, variable=radiostate,
                           command=radiobutton_used)
radiobutton2 = Radiobutton(text="RadioButton2", background="Orange", value=2, variable=radiostate,
                           command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()


# ListBox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4, background="Green")
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
