import tkinter as tk
from tkinter import filedialog as fd
import os

class Main(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame_files = tk.Frame(self.master, borderwidth=1, relief="solid")
        self.dir="gam"
        self.files = []

        self.button1 = tk.Button(self.frame, text="Open Anime Directory", command=self.select_file)
        self.label1 = tk.Label(self.frame, text=self.dir, padx=100, borderwidth=1, relief="solid")
        self.label1.grid(row=0,column=0)
        self.button1.grid(row=1,column=0)
        self.frame.grid(row=0, column=0, padx=50)
        self.frame_files.grid(row=2, column=0, pady=50)

    def display_files(self):
        try:
            self.files = os.listdir(self.dir)
            for filename in self.files:
                file_button = tk.Button(self.frame, text=filename)
                file_button.grid(sticky="w")
                self.frame_files.grid(row=2, column=0, pady=50)
                print(filename)
        except OSError:
            print("Failed to display files")


    def select_file(self):
        self.dir = fd.askdirectory(
            title="Open a file",
            initialdir="/",
        )
        self.label1["text"] = self.dir
        self.display_files()


if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.geometry("1280x720")
    root.rowconfigure(0, minsize=50)
    root.mainloop()




