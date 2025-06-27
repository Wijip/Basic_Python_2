import tkinter as tk
from tkinter import messagebox, filedialog

# Fungsi untuk membuat file baru dan memasukkan data ke dalamnya
def create_file():
    file_name = entry_filename.get()
    if file_name:
        with open(file_name + '.txt', 'w') as file:
            data = text_area.get("1.0", tk.END)
            file.write(data)
        messagebox.showinfo("Info", "File created successfully")

# Fungsi untuk menambahkan data ke file yang ada
def append_to_file():
    file_name = entry_filename.get()
    if file_name:
        with open(file_name + '.txt', 'a') as file:
            data = text_area.get("1.0", tk.END)
            file.write(data)
        messagebox.showinfo("Info", "Data appended successfully")

# Fungsi untuk mengganti data dalam file yang ada
def update_file():
    file_name = entry_filename.get()
    if file_name:
        with open(file_name + '.txt', 'r') as file:
            lines = file.readlines()

        search_text = entry_search.get()
        update_text = entry_update.get()
        updated_lines = [line.replace(search_text, update_text) for line in lines]

        with open(file_name + '.txt', 'w') as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Info", "File updated successfully")

# Fungsi untuk membaca dan menampilkan data dari file
def read_file():
    file_name = entry_filename.get()
    if file_name:
        with open(file_name + '.txt', 'r') as file:
            data = file.read()
            display_area.delete("1.0", tk.END)
            display_area.insert(tk.END, data)
        messagebox.showinfo("Info", "File read successfully")

# Fungsi untuk menghapus data tertentu dari file
def delete_from_file():
    file_name = entry_file.get()
    if file_name:
        with open(file_name + '.txt', 'r') as file:
            lines = file.readlines()

        delete_text = entry_delete.get().strip()
        updated_lines = [line for line in lines if line.strip() != delete_text]

        with open(file_name + '.txt', 'w') as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Info", "Data deleted successfully")

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("GUI CRUD")

# Frame untuk bagian atas
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Nama file:").grid(row=0, column=0, sticky=tk.W)
entry_filename = tk.Entry(top_frame)
entry_filename.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Teks:").grid(row=1, column=0, sticky=tk.W)
text_area = tk.Text(top_frame, height=10, width=30)
text_area.grid(row=2, column=0, columnspan=2)

# Frame untuk bagian tengah
middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

tk.Label(middle_frame, text="Tampil:").grid(row=0, column=0, sticky=tk.W)
display_area = tk.Text(middle_frame, height=10, width=30)
display_area.grid(row=1, column=0, columnspan=2)

# Frame untuk tombol-tombol
button_frame = tk.Frame(middle_frame)
button_frame.grid(row=2, column=0, columnspan=2)

create_button = tk.Button(button_frame, text="Create", command=create_file)
create_button.grid(row=0, column=0, padx=5, pady=5)

append_button = tk.Button(button_frame, text="Append", command=append_to_file)
append_button.grid(row=0, column=1, padx=5, pady=5)

read_button = tk.Button(button_frame, text="Read", command=read_file)
read_button.grid(row=0, column=2, padx=5, pady=5)

# Frame untuk bagian bawah
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

tk.Label(bottom_frame, text="Search text:").grid(row=0, column=0, sticky=tk.W)
entry_search = tk.Entry(bottom_frame)
entry_search.grid(row=0, column=1, padx=5)

tk.Label(bottom_frame, text="Update text:").grid(row=1, column=0, sticky=tk.W)
entry_update = tk.Entry(bottom_frame)
entry_update.grid(row=1, column=1, padx=5)

update_button = tk.Button(bottom_frame, text="Update", command=update_file)
update_button.grid(row=1, column=2, padx=5, pady=5)

tk.Label(bottom_frame, text="File:").grid(row=2, column=0, sticky=tk.W)
entry_file = tk.Entry(bottom_frame)
entry_file.grid(row=2, column=1, padx=5)

tk.Label(bottom_frame, text="Delete text:").grid(row=3, column=0, sticky=tk.W)
entry_delete = tk.Entry(bottom_frame)
entry_delete.grid(row=3, column=1, padx=5)

delete_button = tk.Button(bottom_frame, text="Delete", command=delete_from_file)
delete_button.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()
