import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Text Editor")
        self.geometry("600x400")
        self.text = tk.Text(self, wrap="word")
        self.text.pack(fill="both", expand=True)
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())
            self.title(f"Simple Text Editor - {path}")

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if path:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.text.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"File saved to {path}")
            self.title(f"Simple Text Editor - {path}")

if __name__ == "__main__":
    TextEditor().mainloop()
