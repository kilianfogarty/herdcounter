import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from utils import get_image_paths
from inference import load_image


def select_folder():
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    image_paths = get_image_paths(folder)

    if len(image_paths) == 0:
        messagebox.showwarning("No Images", "No images found in selected folder.")
        return
    
    first_image = load_image(image_paths[0])

    messagebox.showinfo(
        "Images Loaded",
        f"Found {len(image_paths)} images."
    )

root = tk.Tk()
root.title("Herd Counter")
root.geometry("400x400")

title = tk.Label(root, text="Caribou Image Analyzer", font=("Arial", 14))
title.pack(pady=20)

button = tk.Button(root, text="Select Image Folder", command=select_folder)
button.pack()

root.mainloop()