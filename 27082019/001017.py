import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

# se crea un array del 1 al 5
z = np.array([1,2,3,4,5])							
print z < 3	
print z > 3											
photo = imread('skimage/imagen.png') 		
photo_masked = np.where(photo > 100,255,100)
plt.imshow(photo_masked)							
plt.show()