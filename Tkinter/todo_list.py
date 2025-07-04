import tkinter as tk
from tkinter import messagebox

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("300x400")

        self.entry = tk.Entry(self)
        self.entry.pack(fill="x", padx=5, pady=5)
        tk.Button(self, text="Add", command=self.add_task).pack(fill="x", padx=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)

        frame = tk.Frame(self)
        frame.pack(fill="x", padx=5, pady=5)
        tk.Button(frame, text="Delete Selected", command=self.delete_task).pack(side="left", expand=True)
        tk.Button(frame, text="Save", command=self.save_tasks).pack(side="left", expand=True)
        tk.Button(frame, text="Load", command=self.load_tasks).pack(side="left", expand=True)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def delete_task(self):
        sel = self.listbox.curselection()
        for i in reversed(sel):
            self.listbox.delete(i)

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in self.listbox.get(0, tk.END):
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                lines = [l.strip() for l in f if l.strip()]
            self.listbox.delete(0, tk.END)
            for task in lines:
                self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showwarning("No file", "tasks.txt not found.")

if __name__ == "__main__":
    TodoListApp().mainloop()
