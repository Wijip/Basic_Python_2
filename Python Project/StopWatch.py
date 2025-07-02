import tkinter as tk
from tkinter import messagebox

class StopwatchTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch & Timer")
        self.mode = tk.StringVar(value="stopwatch")

        # Mode selection
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Radiobutton(frame, text="Stopwatch", variable=self.mode, value="stopwatch",
                       command=self.reset).pack(side="left")
        tk.Radiobutton(frame, text="Timer", variable=self.mode, value="timer",
                       command=self.reset).pack(side="left")

        # Timer input (menit)
        self.timer_entry = tk.Entry(self, width=5)
        self.timer_entry.pack()
        self.timer_entry.insert(0, "1")  # default 1 minute

        # Display label
        self.label = tk.Label(self, text="00:00", font=("Arial", 36))
        self.label.pack(pady=10)

        # Control buttons
        ctrl = tk.Frame(self)
        ctrl.pack()
        tk.Button(ctrl, text="Start", command=self.start).pack(side="left", padx=5)
        tk.Button(ctrl, text="Stop",  command=self.stop).pack(side="left", padx=5)
        tk.Button(ctrl, text="Reset", command=self.reset).pack(side="left", padx=5)

        # Internal counters
        self.running = False
        self.elapsed = 0       # untuk stopwatch (detik)
        self.remaining = 0     # untuk timer (detik)

    def update(self):
        if not self.running:
            return

        if self.mode.get() == "stopwatch":
            self.elapsed += 1
            minutes = self.elapsed // 60
            seconds = self.elapsed % 60
        else:  # timer mode, berjalan mundur
            # initialize remaining jika belum di-set
            if self.remaining <= 0:
                try:
                    total_min = int(self.timer_entry.get())
                except ValueError:
                    messagebox.showerror("Invalid input", "Masukkan angka menit untuk timer.")
                    self.stop()
                    return
                self.remaining = total_min * 60

            # kurangi satu detik
            self.remaining -= 1
            if self.remaining < 0:
                # timer selesai
                self.stop()
                messagebox.showinfo("Timer", "Waktu habis!")
                self.remaining = 0

            minutes = self.remaining // 60
            seconds = self.remaining % 60

        # update tampilan
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")
        # jadwalkan update berikutnya
        self.after(1000, self.update)

    def start(self):
        if not self.running:
            self.running = True
            # reset counters saat mulai pertama kali di timer
            if self.mode.get() == "timer":
                try:
                    total_min = int(self.timer_entry.get())
                except ValueError:
                    messagebox.showerror("Invalid input", "Masukkan angka menit untuk timer.")
                    return
                self.remaining = total_min * 60
            self.after(0, self.update)

    def stop(self):
        self.running = False

    def reset(self):
        self.stop()
        self.elapsed = 0
        self.remaining = 0
        self.label.config(text="00:00")

if __name__ == "__main__":
    StopwatchTimer().mainloop()
