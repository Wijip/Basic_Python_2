import tkinter as tk
from tkinter import messagebox

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        tk.Label(self, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.amount_var = tk.StringVar()
        tk.Entry(self, textvariable=self.amount_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Rate:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rate_var = tk.StringVar()
        tk.Entry(self, textvariable=self.rate_var).grid(row=1, column=1, padx=5, pady=5)

        btn = tk.Button(self, text="Convert", command=self.convert)
        btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self, text="Result: ")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

    def convert(self):
        try:
            amt = float(self.amount_var.get())
            rate = float(self.rate_var.get())
            res = amt * rate
            self.result_label.config(text=f"Result: {res:.2f}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter numeric values.")

if __name__ == "__main__":
    CurrencyConverter().mainloop()
