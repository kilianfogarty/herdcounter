import os

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".tif", ".tiff")

def get_image_paths(folder_path):
    #Returns a list of full file paths to each image in a folder

    image_paths = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            full_path = os.path.join(folder_path, filename)
            image_paths.append(full_path)

    return image_paths