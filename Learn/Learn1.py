from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("GUI DEMO")
root.geometry('400x200')
root.resizable(True, True)
"""
X dan Y
"""
# Button(root, text="Left").pack(side=LEFT,expand=YES, fill=Y)
# Button(root, text="Right").pack(side=RIGHT,expand=YES, fill=Y)
# Button(root, text="Top").pack(side=TOP,expand=YES, fill=BOTH)
# Button(root, text="Bottom").pack(side=BOTTOM,expand=YES, fill=BOTH)
label = Label(root, text="Coba Label" ).grid(row=3, column=0)
Button(root, text="1", width=16).grid(row=0, column=0)
Button(root, text="2", width=16).grid(row=1, column=0)
Button(root, text="3", width=16).grid(row=2, column=0)
Button(root, text="4", width=16).grid(row=0, column=1)

# Button(root, text="Button 1").place(x=10, y=10, height=35)
# Button(root, text="Button 2").place(x=100, y=10, height=35)
# Button(root, text="Button 3").place(x=200, y=10, height=35)

# btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy)
# btn.pack(side = 'top')

root.mainloop()