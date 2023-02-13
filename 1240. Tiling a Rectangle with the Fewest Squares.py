""" 1240. Tiling a Rectangle with the Fewest Squares

Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Input: n = 11, m = 13
Output: 6
  """

#直觉填最大可能的squre， 然后递归是错误的
#需要搜索所有可能性
#从bottom到top， 从左到右尝试填充
#一个高度数组height， 记录每一个单位宽度的填充高度, 开始是[0] * W
#dfs(height, fills)， 从height数组和一个填充次数开始， dfs， fills初始是0
#找到高度数组的最低高度， 然后尝试右边的同样高度单元， 从最大可能的squre开始尝试填充， 每次得到一个新的高度数组， 再从新的高度数组和fills+1开始尝试填充

class Solution:

    def tilingRectangle(self, H: int, W: int) -> int:
	    self.best = H * W

	    def dfs(height, moves):
		    if all(h == H for h in height):
    			self.best = min(self.best, moves)
	    		return
		    if moves >= self.best:
			    return
		    min_height = min(height)
		    idx = height.index(min_height)
		    ridx = idx + 1
		    while ridx < W and height[ridx] == min_height:
			    ridx += 1
		    for i in range(min(ridx - idx, H - min_height), 0, -1):
			    new_height = height[:]
			    for j in range(i):
				    new_height[idx + j] += i
			    dfs(new_height, moves + 1) 

	    dfs([0] * W, 0)
	    return self.best