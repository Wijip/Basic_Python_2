import tkinter as tk
from tkinter import messagebox

class FileEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI CRUD")

        # Label dan Entry untuk nama file
        self.nama_file_label = tk.Label(self.window, text="Nama file:")
        self.nama_file_label.grid(row=0, column=0, padx=5, pady=5)

        self.nama_file_entry = tk.Entry(self.window)
        self.nama_file_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label dan Textbox untuk teks
        self.teks_label = tk.Label(self.window, text="Teks:")
        self.teks_label.grid(row=1, column=0, padx=5, pady=5)

        self.teks_entry = tk.Text(self.window, height=5)
        self.teks_entry.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        # Tombol Create
        self.create_button = tk.Button(self.window, text="Create", command=self.create_file)
        self.create_button.grid(row=3, column=0, padx=5, pady=5)

        # Tombol Append
        self.append_button = tk.Button(self.window, text="Append", command=self.append_file)
        self.append_button.grid(row=4, column=0, padx=5, pady=5)

        # Label untuk Tampilan
        self.tampil_label = tk.Label(self.window, text="Tampil:")
        self.tampil_label.grid(row=1, column=2, padx=5, pady=5)

        self.tampil_text = tk.Text(self.window, height=5)
        self.tampil_text.grid(row=2, column=2, padx=5, pady=5)

        # Tombol Read
        self.read_button = tk.Button(self.window, text="Read", command=self.read_file)
        self.read_button.grid(row=2, column=3, padx=5, pady=5)

        # Label dan Entry untuk search text
        self.search_text_label = tk.Label(self.window, text="Search text:")
        self.search_text_label.grid(row=5, column=0, padx=5, pady=5)

        self.search_text_entry = tk.Entry(self.window)
        self.search_text_entry.grid(row=5, column=1, padx=5, pady=5)

        # Label dan Entry untuk update text
        self.update_text_label = tk.Label(self.window, text="Update text:")
        self.update_text_label.grid(row=5, column=2, padx=5, pady=5)

        self.update_text_entry = tk.Entry(self.window)
        self.update_text_entry.grid(row=5, column=3, padx=5, pady=5)

        # Tombol Update
        self.update_button = tk.Button(self.window, text="Update", command=self.update_file)
        self.update_button.grid(row=5, column=4, padx=5, pady=5)

        # Label dan Entry untuk file
        self.file_label = tk.Label(self.window, text="File:")
        self.file_label.grid(row=6, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(self.window)
        self.file_entry.grid(row=6, column=1, padx=5, pady=5)

        # Tombol Delete
        self.delete_button = tk.Button(self.window, text="Delete", command=self.delete_file)
        self.delete_button.grid(row=6, column=2, padx=5, pady=5)

        self.window.mainloop()

    def create_file(self):
        nama_file = self.nama_file_entry.get()
        teks = self.teks_entry.get("1.0", tk.END)
        try:
            with open(nama_file, "w") as file:
                file.write(teks)
            messagebox.showinfo("Sukses", "File berhasil dibuat")
        except:
            messagebox.showerror("Gagal", "Terjadi kesalahan dalam membuat file")

    def append_file(self):
        nama_file = self.nama_file_entry.get()
        teks = self.teks_entry.get("1.0", tk.END)
        try:
            with open(nama_file, "a") as file:
                file.write(teks)
            messagebox.showinfo("Sukses", "Teks berhasil ditambahkan ke file")
        except:
            messagebox.showerror("Gagal", "Terjadi kesalahan dalam menambahkan teks ke file")

    def read_file(self):
        nama_file = self.nama_file_entry.get()
        try:
            with open(nama_file, "r") as file:
                teks = file.read()
                self.tampil_text.delete("1.0", tk.END)
                self.tampil_text.insert(tk.END, teks)
        except:
            messagebox.showerror("Gagal", "Terjadi kesalahan dalam membaca file")

    def update_file(self):
        nama_file = self.nama_file_entry.get()
        teks_baru = self.update_text_entry.get()
        teks_lama = self.search_text_entry.get()
        try:
            with open(nama_file, "r") as file:
                teks = file.read()
            teks = teks.replace(teks_lama, teks_baru)
            with open(nama_file, "w") as file:
                file.write(teks)
            messagebox.showinfo("Sukses", "Teks dalam file berhasil diperbarui")
        except:
            messagebox.showerror("Gagal", "Terjadi kesalahan dalam memperbarui file")

    def delete_file(self):
        nama_file = self.file_entry.get()
        try:
            import os
            os.remove(nama_file)
            messagebox.showinfo("Sukses", "File berhasil dihapus")
        except:
            messagebox.showerror("Gagal", "Terjadi kesalahan dalam menghapus file")

if __name__ == "__main__":
    FileEditor()