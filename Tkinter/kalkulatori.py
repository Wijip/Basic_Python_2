import tkinter as tk

# Fungsi untuk menambahkan angka ke layar kalkulator
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Fungsi untuk melakukan operasi perhitungan
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Fungsi untuk menghapus layar kalkulator
def clear():
    entry.delete(0, tk.END)

# Membuat window
window = tk.Tk()
window.title("Kalkulator")
window.geometry('250x300')
window.resizable(False, False)

# Entry untuk menampilkan hasil perhitungan
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Membuat tombol-tombol kalkulator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_num = 1
col_num = 0

for button_text in buttons:
    tk.Button(window, text=button_text, padx=20, pady=20, command=lambda b=button_text: button_click(b) if b != '=' else calculate() if b != 'C' else clear()).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Menjalankan program
window.mainloop()
