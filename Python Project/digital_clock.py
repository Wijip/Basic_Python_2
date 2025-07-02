import tkinter as tk
import time

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.label = tk.Label(self, font=("Helvetica", 48), bg="black", fg="cyan")
        self.label.pack(fill="both", expand=True)
        self.format_24 = True

        toggle = tk.Button(self, text="Toggle 12/24h", command=self.toggle_format)
        toggle.pack(fill="x")

        self.update_clock()

    def update_clock(self):
        fmt = "%H:%M:%S" if self.format_24 else "%I:%M:%S %p"
        now = time.strftime(fmt)
        self.label.config(text=now)
        self.after(1000, self.update_clock)

    def toggle_format(self):
        self.format_24 = not self.format_24

if __name__ == "__main__":
    DigitalClock().mainloop()
