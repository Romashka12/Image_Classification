import torch
import torchvision
from torchvision import transforms
from os import path

path_to_labels=path.join("..","NN_training","imagenet_classes.txt")
with open(path_to_labels, "r") as f:
    categories = [s.strip() for s in f.readlines()]

loaded_model=torch.load(path.join('..','NN_training','model_weights','mobile_net_v2_no_change.model'))
loaded_model.eval()

preprocess=transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485,0.456,0.406],
                         std=[0.229,0.224,0.225])
])

def get_label(image,categories=categories,preprocess=preprocess):
    input_tensor=preprocess(image)
    input_batch = input_tensor.unsqueeze(0) #needed to work with images of batch size 0
    with torch.no_grad():
        output = loaded_model(input_batch)
        
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    top5_prob, top5_catid = torch.topk(probabilities, 5)
    result = {}
    for i in range(top5_prob.size(0)):
        result[categories[top5_catid[i]]] = top5_prob[i].item()
    return result


