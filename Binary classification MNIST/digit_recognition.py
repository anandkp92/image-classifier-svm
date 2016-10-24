import numpy as np
import struct
import math
import server
import threading

def parse_images(filename):
    f = open(filename,"rb");
    magic,size = struct.unpack('>ii', f.read(8))
    sx,sy = struct.unpack('>ii', f.read(8))
    X = []
    for i in range(size):
        im =  struct.unpack('B'*(sx*sy), f.read(sx*sy))
        X.append([float(x)/256.0 for x in im]);
    return np.array(X);

def parse_labels(filename):
    f = open(filename,"rb");
    magic,size = struct.unpack('>ii', f.read(8))
    return np.array(struct.unpack('B'*size, f.read(size)))

def error(X, y, theta):
    return float(np.sum(np.sign(X.dot(theta)) != y))/y.shape[0]

# implement the functions below
def loss_logistic(X,y,theta):
    l = np.sum(np.log(1 + np.exp(-y * X.dot(theta))))
    z = 1 / (1 + np.exp(y * X.dot(theta)))
    return l/y.shape[0], -X.T.dot(z * y) / y.shape[0]
def loss_svm(X,y,theta):
    z = y*X.dot(theta)
    l = np.sum(np.maximum(0, 1 - z)) / y.shape[0]
    g = -X.T.dot((z < 1) * y) / y.shape[0]
    return l,g
def grad_descent(X, y, lam, loss, T, alpha):
    theta = np.zeros(X.shape[1])
    for _ in xrange(T):
        l,g = loss(X, y, theta)
        theta -= alpha*(g + lam*theta)
    return theta
def stochastic_grad_descent(X, y, lam, loss, T, alpha):
    theta = np.zeros(X.shape[1])
    for _ in xrange(T):
        for i in xrange(X.shape[0]):
            l,g = loss(X[i:i+1,:], y[i:i+1], theta)
            theta -= alpha*(g + lam*theta)
    return theta
    
X = parse_images("train-images-idx3-ubyte")
y = parse_labels("train-labels-idx1-ubyte")


y0 = 1.*(y == 1) - 1.*(y != 1)
theta = stochastic_grad_descent(X, y0, 1e-3, loss_svm, 10, 0.001)
print error(X, y0, theta)
### 0.00783333
theta = grad_descent(X, y0, 1e-3, loss_svm, 10, 5.0)
print error(X, y0, theta)
### 0.01906666
