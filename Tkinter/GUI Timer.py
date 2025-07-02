import tkinter as tk
from tkinter import messagebox
import time
import threading

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer GUI")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.running = False
        self.remaining_time = 0
        self.original_time = 0

        # Frame untuk input menit dan detik
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Menit:").grid(row=0, column=0)
        self.minutes_entry = tk.Entry(input_frame, width=5)
        self.minutes_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Detik:").grid(row=0, column=2)
        self.seconds_entry = tk.Entry(input_frame, width=5)
        self.seconds_entry.grid(row=0, column=3)

        # Label untuk menampilkan timer
        self.timer_label = tk.Label(root, text="00:00", font=("Courier", 32))
        self.timer_label.pack(pady=20)

        # Frame untuk tombol kontrol
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", width=8, command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=8, command=self.stop_timer)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_timer_label(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

    def countdown(self):
        while self.running and self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            self.update_timer_label()

        if self.running and self.remaining_time == 0:
            self.running = False
            messagebox.showinfo("Selesai", "Waktu Sudah Selesai!")

    def start_timer(self):
        if self.running:
            return

        # Ambil nilai baru jika timer belum di-set
        if self.remaining_time == 0:
            try:
                minutes = int(self.minutes_entry.get() or 0)
                seconds = int(self.seconds_entry.get() or 0)
            except ValueError:
                messagebox.showerror("Input Error", "Masukkan angka valid untuk menit dan detik.")
                return

            self.original_time = minutes * 60 + seconds
            self.remaining_time = self.original_time

        self.running = True
        threading.Thread(target=self.countdown, daemon=True).start()
        self.update_timer_label()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        # Hentikan timer
        self.running = False

        # Set ulang ke 00:00
        self.remaining_time = 0
        self.original_time = 0

        # Kosongkan input jika diinginkan
        self.minutes_entry.delete(0, tk.END)
        self.seconds_entry.delete(0, tk.END)

        # Perbarui tampilan timer
        self.update_timer_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
