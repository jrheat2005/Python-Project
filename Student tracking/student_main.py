
from tkinter import *
import tkinter as tk
from tkinter import messagebox


import student_gui
import student_func



class ParentWindow(Frame):
    def __init__(self,master,*args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # defines our master frame configuration
        self.master = master
        self.master.minsize(500,350)
        self.master.maxsize(500,350)
        # centers our app on the screen
        student_func.center_window(self,500,350)
        self.master.title("Stutent Tracking")
        self.master.configure(bg="lightgray")

        student_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
