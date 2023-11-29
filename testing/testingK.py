import tkinter as tk

# Membuat window
window = tk.Tk()
window.title("Kalkulator")

# Fungsi untuk menampilkan pesan ketika tombol ditekan
def tombol_ditekan(text):
    pesan.config(text=f"Tombol {text} ditekan")

# Membuat tombol-tombol angka
angka = "0123456789"
for i in range(10):
    button = tk.Button(window, text=angka[i], command=lambda i=i: tombol_ditekan(angka[i]))
    button.grid(row=i//3, column=i%3)

# Tombol lainnya
tombol_lain = ["+", "-", "*", "/", "=", "C"]
row = 3
col = 0
for operator in tombol_lain:
    button = tk.Button(window, text=operator, command=lambda operator=operator: tombol_ditekan(operator))
    button.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Label untuk pesan
pesan = tk.Label(window, text="", font=("Helvetica", 12))
pesan.grid(row=4, column=0, columnspan=3)

# Menjalankan program
window.mainloop()
