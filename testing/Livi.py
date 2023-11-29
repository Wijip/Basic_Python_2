import tkinter as tk

root = tk.Tk()
root.title('login')
root.geometry("330x250")
teks = tk.StringVar()

label = tk.Label(root, text="please enter details below to login", font=("Times New Roman", 10))
label.grid(row=0,column=1)

username = tk.Label(root, text='username:', font=('calibre',10, 'bold'))
username.grid(row=5,column=0)
username_entry = tk.Entry(root,textvariable = teks, font=('calibre',10,'normal'))
username_entry.grid(row=5,column=1)

password = tk.Label(root, text='password:', font=('calibre',10,'bold'))
password.grid(row=6, column=0)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=6, column=1)

login_button = tk.Button(root, text='Login')
login_button.grid(row=7, column=1)
root.mainloop()
