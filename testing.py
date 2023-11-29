import tkinter as tk

root = tk.Tk()
root.title('Login')
root.geometry('300x200')


label = tk.Label(root, text='Silahkan Login', font=("Time new Rowman", 10))
label.grid(row=0, column=1)

username = tk.Label(root, text='username', font=('arial', 10))
username.grid(row=5,column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=5, column=1)

password = tk.Label(root, text='password', font=('arial',10))
password.grid(row=6, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=6, column=1)

login_button = tk.Button(root, text='Login')
login_button.grid(row=7, column=1)

root.mainloop()
