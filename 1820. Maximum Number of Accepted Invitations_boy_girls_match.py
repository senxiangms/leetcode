""" There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

 

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl. """

#匈牙利算法。 对每个boy dfs(boy, asked_set=set())， dfs里面如果发现有意的女孩没有请求过， 则尝试加match， 通过dfs(matches[girl], asked_set)尝试， 如果另一个男孩
# 还能找到女伴， 则可以成功加match
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:

        matches={}
        G = len(grid[0])
        def dfs(boy, visited):
            for girl in range(G):
                if grid[boy][girl]==1 and girl not in visited:
                    visited.add(girl)
                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True
            return False

        for boy in range(len(grid)):
            dfs(boy, set())
        return len(matches)
