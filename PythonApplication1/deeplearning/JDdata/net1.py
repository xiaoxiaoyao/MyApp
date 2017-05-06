import numpy as np
class Sigmoid():
# Sigmoid函数，S型曲线，sigmoid function
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    # Sigmoid函数的导函数
    def sigmoid_d(self, z,deriv=True):
        return self.sigmoid(z)*(1-self.sigmoid(z))
Sigmoid=Sigmoid()

# input dataset
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
print("input dataset:\n",x) 
# output dataset            
y = np.array([[0,0,0,1]]).T
print("output dataset:\n",y)
 
# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)
 
# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1
 
for iter in range(10000):
    # forward propagation
    l0 = x
    l1 = Sigmoid.sigmoid(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * Sigmoid.sigmoid_d(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
print("Output After Training:")
print(l1)