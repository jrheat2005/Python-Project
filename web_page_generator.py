import tkinter as tk
from tkinter import *
import webbrowser
# creating buttons and text boxs
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))

        self.submit = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.inputHTML)
        self.submit.grid(row=2, column=2, padx=(10,10) , pady=(10,10))

        self.entry = Entry(width=75)
        self.entry.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(5, 0))

        self.text = Label(root, text='Enter custom text below.', font=("Arial", 10))
        self.text.grid(row=0, column=1,pady=(10, 0))

    # default html website hard coded text
    def defaultHTML(self):
        htmlText = "This is a basic html website."
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    # html with user input text
    def inputHTML(self):
        myinput = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + myinput + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
