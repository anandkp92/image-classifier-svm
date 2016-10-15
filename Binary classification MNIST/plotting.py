import numpy as np
import matplotlib.pyplot as plt
from digit_recognition import parse_images

X = parse_images("train-images-idx3-ubyte")

M,N = 10,20
fig, ax = plt.subplots(figsize=(N,M))
digits = np.vstack([np.hstack([np.reshape(X[i*N+j,:],(28,28)) for j in range(N)]) for i in range(M)])
ax.imshow(255-digits, cmap=plt.get_cmap('gray'))
ax.axis('off')
plt.show()

