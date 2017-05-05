import numpy as np
import random

class NeuralNet(object):
    # 初始化神经网络，sizes是神经网络的层数和每层神经元个数
    def __init__(self, sizes):
        self.sizes_ = sizes
        self.num_layers_ = len(sizes)  # 层数
        self.w_ = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]  # w_、b_初始化为正态分布随机数
        self.b_ = [np.random.randn(y, 1) for y in sizes[1:]]

net = NeuralNet ([3,4,4,2])
print ('权重: ' , net.w_,'biases: ' , net.b_)

class Sigmoid():
# Sigmoid函数，S型曲线，
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    # Sigmoid函数的导函数
    def sigmoid_prime(self, z):
        return self.sigmoid(z)*(1-self.sigmoid(z))

sigmoid = Sigmoid()
net.w_ = map(sigmoid.sigmoid,net.w_)
net.b_ = map(sigmoid.sigmoid,net.b_)
print ('权重: ' , net.w_,'biases: ' , net.b_)