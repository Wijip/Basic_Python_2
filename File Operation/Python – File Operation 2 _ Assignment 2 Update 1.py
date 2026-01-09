import tkinter as tk
from tkinter import messagebox

class DataEntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assignment 2 Data Entry")
        self.geometry("350x200")
        self.resizable(False, False)

        tk.Label(self, text="Nama:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.nama_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nama_var, width=30).grid(row=0, column=1)

        tk.Label(self, text="Umur:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.umur_var = tk.StringVar()
        tk.Entry(self, textvariable=self.umur_var, width=30).grid(row=1, column=1)

        tk.Label(self, text="Alamat:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.alamat_var = tk.StringVar()
        tk.Entry(self, textvariable=self.alamat_var, width=30).grid(row=2, column=1)

        submit_btn = tk.Button(self, text="Submit", command=self.save_data)
        submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

    def save_data(self):
        nama = self.nama_var.get().strip()
        umur = self.umur_var.get().strip()
        alamat = self.alamat_var.get().strip()

        if not nama or not umur or not alamat:
            messagebox.showwarning("Input Kosong", "Semua field harus diisi.")
            return

        with open("assignment2.txt", "a", encoding="utf-8") as f:
            f.write(f"{nama} | {umur} | {alamat}\n")

        messagebox.showinfo("Sukses", "Data berhasil disimpan ke file assignment2.txt")

        self.nama_var.set("")
        self.umur_var.set("")
        self.alamat_var.set("")

if __name__ == '__main__':
    app = DataEntryApp()
    app.mainloop()