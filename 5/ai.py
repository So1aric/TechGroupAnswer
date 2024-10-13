#!/usr/bin/env python
# coding: utf-8

# In[88]:


import torch
from torch import nn
import random
import matplotlib.pyplot as plt


# In[89]:


class Approx(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(nn.Linear(1, 1))

    def forward(self, x):
        return self.network(x)


# In[90]:


a = random.uniform(-10, 10)
b = random.uniform(-10, 10)
dataset_x = torch.Tensor([i / 10 for i in range(-100, 100)]).reshape(-1, 1)
dataset_y = torch.Tensor([a * x + b + random.uniform(-2, 2) for x in dataset_x])


# In[91]:


plt.scatter(dataset_x, dataset_y)


# In[92]:


network = Approx()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(network.parameters())
epoch = 2000

network.train()

for e in range(epoch):
    output = network(dataset_x)
    loss = loss_fn(dataset_y, output[:, 0])
    
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    if e % 100 != 0: continue
    print(f'epoch {e}:')
    print(f'    loss: {loss.item()}')
    


# In[93]:


plt.plot(dataset_x, [network(i).item() for i in dataset_x])
plt.show()


# In[ ]:




