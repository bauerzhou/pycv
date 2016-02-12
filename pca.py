from PIL import Image 
from pylab import * 

def pca(X):
	"""主成分析：
	输入： 矩阵X 
	返回：投影矩阵, 方差和均值 """

	#获取维数
	num_data, dim = X.shape 

	#数据中心化 
	mean_X = X.mean(axis=0)
	X = X - mean_X 

	if dim > num_data:
		#PCA-使用紧致技巧 
		M = dot(X, X.T)
		e, EV = linalg.eigh(M) 
		tmp = dot(X.T, EV) 
		V = tmp[::-1]
		S = sqrt(e)[::-1]
		for i in range(V.shape[1]):
			V[:,i] /= S 
	else:
		#PCA-使用SVD方法 
		U,S,V = linalg.svd(X) 
		V = V[:num_data] 

	return V, S, mean_X



