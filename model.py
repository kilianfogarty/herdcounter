import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights

def load_model():
    # Currently loads a pretrained Mask R-CNN model (Will train my own later)

    weights = MaskRCNN_ResNet50_FPN_Weights.DEFAULT
    model = maskrcnn_resnet50_fpn(pweights=weights)
    model.eval() #Inference mode
    return model