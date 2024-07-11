#1. Viết class và cài phương thức softmax
import torch
import torch.nn as nn

class Softmax(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    return torch.exp(x) / torch.sum(torch.exp(x))

class softmax_stable(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    return torch.exp(x - torch.max(x)) / torch.sum(torch.exp(x - torch.max(x)))

data = torch.Tensor ([1 , 2, 3])
softmax = Softmax()
output = softmax (data)
print(output)

data = torch.Tensor([1 , 2, 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
print(output)