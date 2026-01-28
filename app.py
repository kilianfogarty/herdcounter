import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        print("Selected folder:", folder)

root = tk.Tk()
root.title("Herd Counter")
root.geometry("400x400")

title = tk.Label(root, text="Caribou Image Analyzer", font=("Arial", 14))
title.pack(pady=20)

button = tk.Button(root, text="Select Image Folder", command=select_folder)
button.pack()

root.mainloop()