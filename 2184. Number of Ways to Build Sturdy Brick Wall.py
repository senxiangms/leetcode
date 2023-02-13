""" You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:
Input: height = 2, width = 3, bricks = [1,2]
Output: 2
Explanation:
The first two walls in the diagram show the only two ways to build a sturdy brick wall.
Note that the third wall in the diagram is not sturdy because adjacent rows join bricks 2 units from the left. """

#注意要求， sturdy， 就是中间的缝隙不能在相邻行有重合

#第一步求每一层所有可能的砖的缝隙位置， 通过backtrack容易求得
#第二步求每一种铺砖方式 跟其他方式是不是满足条件， 得到一个字典adj[i].append(j)
#第三步， 对每一种铺砖做为起始方式， 求得总体铺砖方法。 
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        combinations = []
        
        def rec(prefix, cur_w):
            if cur_w == width:
                combinations.append(prefix[:])
                return
            for w in bricks:
                if w + cur_w <= width:
                    prefix.append(w+cur_w)
                    rec(prefix, cur_w+w)
                    prefix.pop()
            return
        
        rec([], 0)
        print(combinations)
        N = len(combinations)
        unsturdy = collections.defaultdict(list)
        for i, comb in enumerate(combinations):
            for j, neighbor in enumerate(combinations):
                # check if bricks at the same location
                if len(set(comb[:-1]) & set(neighbor[:-1])) == 0:
                    unsturdy[i].append(j)
        #print(unsturdy)
        
        @cache
        def rec(row, h):
            if h == height:
                return 1
            cur = 0
            for i in unsturdy[row]:
                cur += rec(i, h + 1)
            return cur
        
        ans = 0
        mod = (10**9 + 7)
        for i in range(N):
            ans += rec(i, 1) % mod
        
        return ans % mod

        
        



