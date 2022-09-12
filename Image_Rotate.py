### PROMPT ###

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

### CONSTRAINTS ###
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

import numpy as np

pic = np.array([[1,2,3],[4,5,6],[7,8,9]])
pic2 = ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(pic)
print(np.rot90(pic,k=-1))

# Not that efficient more efficient would be transposing then flipping about the y axis (reverse rows)
# Most efficient would be modifying it in C either using transposes and flipping or rotation matrices