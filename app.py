import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from utils import get_image_paths
from utils import count_animals

from inference import load_image
from inference import run_inference
from inference import filter_predictions

from model import load_model

from annotate import annotate_image

import os


def select_folder():
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    image_paths = get_image_paths(folder)

    if len(image_paths) == 0:
        messagebox.showwarning("No Images", "No images found in selected folder.")
        return
    
    output_dir = os.path.join(folder, "annotated")
    os.makedirs(output_dir, exist_ok=True)

    total_count = 0

    for image_path in image_paths:
        image_tensor = load_image(image_path)
        predictions = run_inference(model, image_tensor)
        filtered = filter_predictions(predictions, score_threshold=0.5)

        count = count_animals(filtered)
        total_count += count

        output_path = os.path.join(output_dir, os.path.basename(image_path))

        annotate_image(image_path, filtered, output_path)

    messagebox.showinfo(
        "Done",
        f"Processed {len(image_paths)} images.\n"
        f"Total detected animals: {total_count}"
    )

model = load_model()

root = tk.Tk()
root.title("Herd Counter")
root.geometry("400x400")

title = tk.Label(root, text="Caribou Image Analyzer", font=("Arial", 14))
title.pack(pady=20)

button = tk.Button(root, text="Select Image Folder", command=select_folder)
button.pack()

root.mainloop()