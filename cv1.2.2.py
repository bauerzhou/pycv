from PIL import Image 
from pylab import * 

im = array(Image.open('psb-3.jpeg').convert('L'))

figure()

gray() 

contour(im, origin='image')
axis('equal')
axis('off')	
#show()

figure() 
hist(im.flatten(), 128)
show()