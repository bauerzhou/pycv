from PIL import Image 
from pylab import * 

def imresize(im, sz):
	"""使用PIL对象重新定义图像数组大小"""
	pil_im = Image.fromarray(uint8(im))

	return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
	"""对一幅图像进行直方图均衡化"""

	#计算图像的直方图
	imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
	cdf = imhist.cumsum()
	cdf = 255 * cdf / cdf[-1] #归一化
	#使用累积分布函数的线性插值，计算新的像素值 
	im2 = interp(im.flatten(), bins[:-1], cdf)

	return im2.reshape(im.shape), cdf 

def compute_average(imlist):
	#计算图像列表的平均图像 
	averageim = array(Image.open(imlist[0]), 'f')

	for imname in imlist[1:]:
		try:
			averageim += array(Image.open(imname))
		except:
			print imname + '...skipped'
		averageim /= len(imlist)

	return array(averageim, 'uint8')



