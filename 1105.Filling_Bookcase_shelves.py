""" 1105. Filling Bookcase Shelves
Medium
1.5K
102
company
Google
company
Bloomberg
company
Amazon
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf. """
import math
class Solution:
    def minHeightShelves(self, books, shelfWidth) -> int:
        N = len(books)
        dp = [math.inf for _ in range(N)]
        if N == 0: return 0
        dp[0] = books[0][1]
        for i in range(1, N):
            th, h = books[i]
            leftwidth = shelfWidth - th
            maxheight = h
            dp[i] = dp[i-1]+ h
            for j in range(i-1, -1, -1):
                th2, h2 = books[j]
                if leftwidth >= th2:
                    leftwidth -= th2
                    maxheight = max(maxheight, h2)
                    dp[i] = min(dp[i], dp[j-1] if j >=1 else 0 + maxheight)
                else:
                    dp[i] = min(dp[i], dp[j] + maxheight)
                    break
        return dp[-1]

                


books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
sol = Solution()
sol.minHeightShelves(books, 4)