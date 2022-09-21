#!/user/bin/env python3
# -*- coding: utf-8 -*-

import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor * tensor)
v_out = torch.mean(variable * variable)
v_out.backward() # 模拟 v_out 的误差反向传递

print(t_out)
print(v_out)
print(tensor)
print(variable)
print(variable.grad)

print(variable)     #  Variable 形式
"""
Variable containing:
 1  2
 3  4
[torch.FloatTensor of size 2x2]
"""

print(variable.data)    # tensor 形式
"""
 1  2
 3  4
[torch.FloatTensor of size 2x2]
"""

print(variable.data.numpy())    # numpy 形式
"""
[[ 1\.  2.]
 [ 3\.  4.]]
"""