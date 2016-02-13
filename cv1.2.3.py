from PIL import Image 
from pylab import * 

im = array(Image.open('psb-3.jpeg'))
imshow(im)

print 'please clieck 3 points'

x=ginput(3)
print 'you clicked:',x 
show()
