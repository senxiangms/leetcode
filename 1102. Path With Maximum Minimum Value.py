""" Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.

Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow. 

Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
 
Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3 """

#从结束点bfs， 如果让周围的点score变更大， 则进deque bfs， 否则丢弃
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = [[-math.inf for _ in range(C)] for _ in range(R)]
        res[R-1][C-1] = grid[R-1][C-1]

        q = collections.deque()
        q.append((R-1, C-1))
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def valid(y, x):
            return 0<=y < R and 0<=x < C 
        while q:
            y, x = q.popleft()
            score = res[y][x]
            for d in dirs:
                dy = y + d[0]
                dx = x + d[1]
                if valid(dy, dx) and res[dy][dx] < min(grid[dy][dx], score):
                    res[dy][dx] = min(grid[dy][dx], score)
                    q.append((dy, dx))
        
        return res[0][0]
