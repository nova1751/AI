#!/user/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
import torch

np_data = np.arange(6).reshape((2, 3))  # 建立numpy数组
torch_data = torch.from_numpy(np_data)  # 将numpy数组转化为torch数据类型
tensor2array = torch_data.numpy()  # 再将torch数据类型转化为numpy类型

data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)  # 转换为32位浮点 tensor

data = [[1, 2],
        [3, 4]]
tensor = torch.FloatTensor(data)
print(np.matmul(data, data), torch.mm(tensor, tensor))

# print(np.abs(data), torch.abs(tensor))
# print(np.sin(data), torch.sin(tensor))
# print(np.mean(data), torch.mean(tensor))
#
# print(np_data)
# print(torch_data)
# print(tensor2array)
