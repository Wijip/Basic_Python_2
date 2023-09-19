import tkinter as tk

root=tk.Tk()
root.geometry("200x100")
teks=tk.StringVar()

name_label = tk.Label(root, text = 'Nama ', font=('calibre',10, 'bold'))

# name_entry = tk.Entry(root,textvariable = teks, font=('calibre',10,'normal'))
name_entry = tk.Entry(root,textvariable = teks)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
root.mainloop()