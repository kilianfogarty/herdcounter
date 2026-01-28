from PIL import Image
import numpy as np
import torch

MAX_RGB = 255.0

def load_image(image_path):
    # Loads image and converts it to a PyTorch tensor.

    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    # Divide by MAX_RGB to normalize between 0 and 1
    image_tensor = torch.from_nupy(image_array).float() / MAX_RGB

    # Change from CHW to HWC (Default for Pytorch but not Pillow)
    image_tensor = image_tensor.permute(2,0,1)

    return image_tensor