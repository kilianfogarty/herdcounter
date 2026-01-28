import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn

def load_model():
    # Currently loads a pretrained Mask R-CNN model (Will train my own later)

    model = maskrcnn_resnet50_fpn(pretrained=True)
    model.eval() #Inference mode
    return model