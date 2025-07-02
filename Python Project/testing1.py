import tkinter as tk
from tkinter import colorchooser

class DrawApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas Drawing App")
        self.width = 800; self.height = 600
        self.canvas = tk.Canvas(self, bg="white", width=self.width, height=self.height)
        self.canvas.pack(side="left", fill="both", expand=True)
        control = tk.Frame(self)
        control.pack(side="right", fill="y")
        tk.Button(control, text="Clear", command=self.clear).pack(pady=5)
        tk.Button(control, text="Color", command=self.choose_color).pack(pady=5)
        self.thickness = tk.Scale(control, from_=1, to=20, orient="horizontal", label="Thickness")
        self.thickness.set(5)
        self.thickness.pack(pady=5)
        self.pen_color = "black"
        self.old_x = None; self.old_y = None
        self.canvas.bind("<ButtonPress-1>", self.start)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, 'old_x', None))

    def start(self, event):
        self.old_x, self.old_y = event.x, event.y

    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.thickness.get(), fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=True)
            self.old_x, self.old_y = event.x, event.y

    def clear(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.pen_color = color

if __name__ == "__main__":
    DrawApp().mainloop()
