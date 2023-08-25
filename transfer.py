# importing
import tkinter as tk
from tkinter import *
import os, shutil
from datetime import timedelta, datetime
from tkinter import filedialog

# button creating and layout
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 0))

        transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
    # source function
    def sourceDir(self):
        selectSourceDir = filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)
    # destination function
    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)
    # file transfer and time check function
    def transferFiles(self):
        source_path = self.source_dir.get()
        dest_path = self.destination_dir.get()

        current_time = datetime.now()

        files_to_transfer = []
        for filename in os.listdir(source_path):
            file_path = os.path.join(source_path, filename)

            file_modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            time_difference = current_time - file_modification_time


            if time_difference.total_seconds() <= 24 * 60 * 60:
                files_to_transfer.append(filename)

        for filename in files_to_transfer:
            source_file_path = os.path.join(source_path, filename)
            dest_file_path = os.path.join(dest_path, filename)
            shutil.move(source_file_path, dest_file_path)
            print(f"Transferred: {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
