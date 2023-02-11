""" You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9. """

#对每一行求一个结果数组result_arr[i]+=points[y][i] , 从左往右result_arr[i]=max(result_arr[i], result_arr[i-1]-1), 再从右往左result_arr[i]=max(result_arr[i], result_arr[i+1]-1)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        C = len(points[0])
        R = len(points)
        res = [0 for _ in range(C)]

        for row in points:
            for x in range(C):
                res[x] += row[x]
                if x > 0:
                    res[x] = max(res[x], res[x-1]-1)
            for x in range(C-2, -1, -1):
                res[x] = max(res[x], res[x+1]-1)
        
        return max(res)

        mem={}
        def dp(row, prev_col):
            if (row, prev_col) in mem:
                return mem[row, prev_col]
            if row == R: 
                return 0
            mx = 0
            for col in range(C):
                n  = points[row][col]
                cost = abs(col-prev_col) if prev_col != -1 else 0
                cur = n + dp(row+1, col) - cost
                mx = max(cur, mx)
            mem[row, prev_col] = mx
            return mx
        return dp(0, -1)