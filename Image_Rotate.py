import numpy as np

pic = np.array([[1,2,3],[4,5,6],[7,8,9]])
pic2 = ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(pic)
print(np.rot90(pic,k=3))

# Not that efficient more efficient would be transposing then flipping about the y axis (reverse rows)