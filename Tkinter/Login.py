import tkinter as tk
from tkinter import messagebox

# Fungsi untuk melakukan login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Ganti dengan logika login yang sesuai
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Membuat window
window = tk.Tk()
window.title("Login")

# Label Username
username_label = tk.Label(window, text="Username:")
username_label.pack()

# Entry untuk Username
username_entry = tk.Entry(window)
username_entry.pack()

# Label Password
password_label = tk.Label(window, text="Password:")
password_label.pack()

# Entry untuk Password
password_entry = tk.Entry(window, show="*")  # Menyembunyikan karakter password
password_entry.pack()

# Tombol Login
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Menjalankan program
window.mainloop()
