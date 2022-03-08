# -*- coding: utf-8 -*-
"""numpy_nn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1quq2mMlgozq-7OrqjcUZlMNtN_a_piqP

### Zadania

1. Dodać iteracje do treningu
2. Dodać rysunek zmian strat w kolejnych iteracjach
"""

import numpy as np
import matplotlib.pyplot as plt

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 16, 4, 0, 1

# Create random input and output data

x_numpy = np.array(    [[0., 0., 0., 1.],
                        [1., 0., 0., 1.],
                        [0., 1., 0., 1.],
                        [0., 0., 1., 1.],
                        [1., 1., 0., 1.],
                        [1., 0., 1., 1.],
                        [0., 1., 1., 1.],
                        [1., 1., 1., 1.],
                        [0., 0., 0., 0.],
                        [1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [1., 1., 0., 0.],
                        [1., 0., 1., 0.],
                        [0., 1., 1., 0.],
                        [1., 1., 1., 0.]])

print(x_numpy.shape)

y_numpy = np.array(     [[1.],
                         [1.],
                         [1.],
                         [1.],
                         [1.],
                         [1.],
                         [1.],
                         [1.],
                         [0.],
                         [0.],
                         [0.],
                         [0.],
                         [0.],
                         [0.],
                         [0.],
                         [0.]])


print(y_numpy.shape)

# Randomly initialize weights
w = np.random.randn(D_in, D_out)

print(w)
print(w.shape)

learning_rate = 1e-5
loss_list = []

# Forward pass: compute predicted y
y_pred = x_numpy.dot(w)
print(y_pred)

# Compute and print loss
loss = np.square(y_pred - y_numpy).sum()

# Backprop to compute gradients of w1 and w2 with respect to loss
grad_y_pred = 2.0 * (y_pred - y_numpy)
grad_w = x_numpy.T.dot(grad_y_pred)

# Update weights
w = w - learning_rate * grad_w
print(w)



plt.plot(loss_list, label = 'loss')
plt.legend()
plt.show()

