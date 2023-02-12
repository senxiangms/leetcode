""" You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2). """

#bfs with 点位置， 此次距离， 此次消除的障碍， 要么距离近， 要么消去的障碍少， 才有机会进队列。 

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dist = {}
        removal ={}
        
        dirs = [[-1,0], [0,-1], [1,0], [0,1]]
        R=len(grid)
        C = len(grid[0])
        q = deque()
        q.append((0,0, R-1, C-1))
        dist[R-1, C-1] = 0
        removal[R-1, C-1] = 0
        while q:
            #print(q)
            dis, rem, y, x = q.popleft()
            if y == 0 and x == 0: return dis
            for dy, dx in dirs:
                ny = y+dy
                nx = x+dx
                nd = dis+1
                nrem = rem
                if 0<=ny<R and 0<=nx<C:
                    if grid[ny][nx] == 1:
                        nrem+=1
                    if (ny, nx) in dist:
                        if nrem <=k and (nd < dist[ny, nx] or nrem<removal[ny,nx]):
                            q.append((nd, nrem, ny, nx))
                            dist[ny,nx]=nd
                            removal[ny,nx] = nrem
                    else:
                        if nrem<=k:
                            q.append((nd, nrem, ny, nx))
                            dist[ny,nx]=nd
                            removal[ny,nx] = nrem
        return -1