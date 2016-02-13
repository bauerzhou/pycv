from scipy.ndimage import filters 

def compute_harris_response(im, sigma=3):
	#在一幅灰度图像中，对每个像素计算Harris角点检测器响应函数

	#计算导数
	imx = zeros(im.shape)
	filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)
	imy = zeros(im.shape)
	filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)

	#计算harris矩阵的分量
	Wxx = filters.gaussian_filter(imx*imx, sigma)
	Wxy = filters.gaussian_filter(imx*imy, sigma)
	Wyy = filters.gaussian_filter(imy*imy, sigma)

	#计算特征值和积
	Wdet = Wxx * Wyy - Wxy ** 2 
	Wtr = Wxx + Wyy 

	return Wdet / Wtr 

def get_harris_points(harrisim, min_dist=10, threshold=0.1):
	#从一幅

	corner_hreshold = harrisim.max() * threshold 
	
