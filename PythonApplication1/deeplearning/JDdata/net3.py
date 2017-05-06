import numpy as np
deriv, z=[None, None]
class Sigmoid():
#Sigmoid函数，S型曲线，sigmoid function
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    # Sigmoid函数的导函数
    def sigmoid_d(self, z, deriv=True):
        return self.sigmoid(z)*(1-self.sigmoid(z))
Sigmoid=Sigmoid()

X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])
print("input dataset:\n",X) 
y = np.array([[0],
            [1],
            [1],
            [0]])
print("output dataset:\n",y)
np.random.seed(10)
 
# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
 
for j in range(60000):
 
    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = Sigmoid.sigmoid(np.dot(l0,syn0))
    l2 = Sigmoid.sigmoid(np.dot(l1,syn1))
 
    # how much did we miss the target value?
    l2_error = y - l2
 
    if (j% 10000) == 0:
        print("Error:",str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*Sigmoid.sigmoid_d(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    # 第  43  行：通过对  l2  层的误差进行“置信度加权”，构建  l1  层相应的误差。为了做到这点，只要简单的通过 l2 与 l1 间的连接权值来传递误差。这种做法也可称作“贡献度加权误差”，因为我们学习的是，l1 层每一个结点的输出值对 l2 层节点误差的贡献程度有多大。接着，用之前 2 层神经网络实现中的相同步骤，对 syn0 权值矩阵进行更新。
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * Sigmoid.sigmoid_d(l1,deriv=True)
    
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)