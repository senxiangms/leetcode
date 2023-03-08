""" You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

 

Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

 """
#dfs(x, y) = dfs(x+1, y) or dfs(x, y+1) if x,y!=0,0 else not(dfs(1,0) and dfs(0,1))
#如果1，0  0，1都有不重合的路径到右下， 肯定不能disconnect
#否则肯定能断链
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 2:
            return False
        
        
        def dfs(i=0,j=0):
            if i == m-1 and j == n-1:
                return True
            
            if i >= m or j >= n or grid[i][j]==0:
                return False
            
            grid[i][j]=0 #Blocking the point. So we do not visit it later.
            
            if (i, j) != (0, 0):
                #If we are not at start, we need to only check that whether this path leads to the end or not. We do not need to check whether more than one path leads to the end or not because if we flip this point, all the paths will be blocked going through the point.
                if dfs(i+1, j):
                    return True
                return dfs(i, j+1)

            #In case of start, if only one path leads to end, we can flip that so to be impossible in one flip both the paths must go to the end.
            return not(dfs(i+1, j) and dfs(i, j+1))
            
        return dfs()