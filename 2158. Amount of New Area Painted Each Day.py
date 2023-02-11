""" There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.

 

Example 1:
Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 
Example 2:
Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. 
Example 3:
Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.

 """

 #一种方法用区间二叉搜索树（最好是平衡树）， 插入每个区间， 并去除掉重合的部分， 只插入新增的区间。
 #用sortedlist， 先把每个区间的起始节点， 结束节点（pos, i, type=-1or1) 排序， 然后从0 开始扫描到最后一个区间的结束位置， 对每个点判断是否区间结束开始， 如果是开始， 
 # 插入开始点的索引到sortedlist。 
 # 需要paint的每个点都加到sortedlist的第一个索引身上。 如果是结束区间， 则从sortedlist里去除。 
import sortedcontainers

class TreeNode:
    def __init__(self, start, end) -> None:
        self.s = start
        self.e = end
        self.left = None
        self.right = None


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        rt = None
        def insert(rt, start, end):
            if rt is None:
                rt = TreeNode(start, end)
                return rt, end - start
            if end <= rt.s:
                rt.left, work = insert(rt.left, start, end)
                return rt, work
            if start >= rt.e:
                rt.right, work = insert(rt.right, start, end)
                return rt, work
            s1, e1 = start, rt.s
            s2, e2 = rt.e, end
            work = 0
            if s1 < e1:
                rt.left, work = insert(rt.left, s1, e1)
            ans = work
            if s2 < e2:
                rt.right, work = insert(rt.right, s2, e2)
                ans += work
            return rt, ans

        ans = []
        for p in paint:
            rt, work = insert(rt, p[0], p[1])
            ans.append(work)
        return ans


        # constructure the sweep line
        records = []
        max_pos = 0
        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1)) # use 1 and -1 to records the type.
            records.append((end, i, -1))
            max_pos = max(max_pos, end)
        records.sort()

        # sweep across all position
        ans = [0 for _ in range(len(paint))]
        indexes = sortedcontainers.SortedList()
        i = 0
        for pos in range(max_pos + 1):
            while i < len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    indexes.add(index)
                else:
                    indexes.remove(index)
                i += 1
            if indexes:
                ans[indexes[0]] += 1
        return ans