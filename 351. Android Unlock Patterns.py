""" Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.
Here are some example valid and invalid unlock patterns:



The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

 

Example 1:

Input: m = 1, n = 1
Output: 9
Example 2:

Input: m = 1, n = 2
Output: 65

 """
 #对每个中间有障碍的数对， 记录数对到障碍的字典比如1,3-->2   1,7-->4
 #然后对1~9做dfs， 注意visited集合要回退 ， dfs的时候判断count是不是在m， n之间

 class Solution:
    def __init__(self):
        self.has_obstacle = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,7):5, (3,1):2, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,7):8, (9,3):6, (9,1):5}
 
    def rec(self, start, count, m, n):
        if m <= count <= n:
            self.ans += 1
        if count == n:
            return
        self.visited.add(start)
        for nxt in range(1, 10):
            if nxt in self.visited:
                continue
            if (start, nxt) in self.has_obstacle:
                if self.has_obstacle[(start,nxt)] in self.visited:
                    self.rec(nxt, count+1, m, n)
            else:
                self.rec(nxt, count+1, m, n)
        self.visited.remove(start)

    def numberOfPatterns(self, m: int, n: int) -> int:
        self.visited=set()
        self.ans = 0
        for start in range(1, 10):
           self.rec(start, 1, m, n)
        return self.ans