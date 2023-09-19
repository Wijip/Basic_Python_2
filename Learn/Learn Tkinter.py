import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Combobox')
window.geometry('500x100')

ttk.Label(window, text = "Select the Month :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)

n = tk.StringVar()
coursechoosen = ttk.Combobox(window, width = 27, textvariable = n)

coursechoosen['values'] = (' Basic Python Programming',
						' C Programming',
						' Pyhton Data Analyst',
						' Coding Explorer',
                        ' Arduino Beginner',)
coursechoosen.grid(column = 1, row = 5)
coursechoosen.current(0)
window.mainloop()