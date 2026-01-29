import numpy as np
import cv2
import torch

def annotate_image(image_path, predictions, output_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masks = predictions["masks"]
    scores = predictions["scores"]

    for i in range(len(masks)):
        mask = masks[i, 0]

        # Convert mask to binary
        mask = mask > 0.5
        mask = mask.cpu().numpy().astype(np.uint8)

        # Create color overlay
        color = np.random.randint(0, 255, size=(3,), dtype=np.uint8)
        overlay = np.zeros_like(image, dtype=np.uint8)
        overlay[mask == 1] = color

        # Blend with original image
        image = cv2.addWeighted(image, 1.0, overlay, 0.5, 0)

    # Save result
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, image)