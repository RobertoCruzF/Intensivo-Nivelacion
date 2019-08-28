import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

a_array = np.array([1,2,3,4,5])    			
b_array = np.array([6,7,8,9,10])	
c_array = a_array + b_array									
d_array = a_array + 30						
e_array = a_array * b_array	
f_array = a_array * 10	

total = 0													
for i in range(0,len(e_array)):								
	total += e_array[i]										

#g_aaray = a_array  b_array
print c_array,"\n", d_array,"\n", e_array, "\n", f_array	
print total

photo = imread('skimage/imagen.png')						
plt.imshow(photo[:,:,0].T)									
plt.show()

x = np.array([2,1,4,3,5])									
y = np.sort(x)				