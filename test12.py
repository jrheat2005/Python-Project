import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __intit__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

self.sourceDir_btn - Button(text-"Select Source", width-20)
self.sourceDir_btn.grid(row-0, column-0, padx-(20, 10), pady-(30, 0))
self.source_dir = Entry(width=75)
self.source_dir.grid(row-0, column-1, columnspan-2, padx-(20, 10), pady-(30, 0))
