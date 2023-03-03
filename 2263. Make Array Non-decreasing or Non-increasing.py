""" You are given a 0-indexed integer array nums. In one operation, you can:

Choose an index i in the range 0 <= i < nums.length
Set nums[i] to nums[i] + 1 or nums[i] - 1
Return the minimum number of operations to make nums non-decreasing or non-increasing.

 

Example 1:

Input: nums = [3,2,4,5,0]
Output: 4
Explanation:
One possible way to turn nums into non-increasing order is to:
- Add 1 to nums[1] once so that it becomes 3.
- Subtract 1 from nums[2] once so it becomes 3.
- Subtract 1 from nums[3] twice so it becomes 3.
After doing the 4 operations, nums becomes [3,3,3,3,0] which is in non-increasing order.
Note that it is also possible to turn nums into [4,4,4,4,0] in 4 operations.
It can be proven that 4 is the minimum number of operations needed.
Example 2:

Input: nums = [2,2,3,4]
Output: 0
Explanation: nums is already in non-decreasing order, so no operations are needed and we return 0.
Example 3: """

#问题简化为求变为上升序列需要的操作数， 因为对nums[::-1]做即是下降序列
#对每个数， 找upward free 数列的最大值， 差值则为cost
class Solution:
    def convertArray(self, nums) -> int:
        def helper(nums):
            que = [] # stores negative number, to make max heap.
            res = 0
            for num in nums:
                if que and num<(-que[0]):
                    res += abs(num-(-heapq.heappop(que)))
                    heapq.heappush(que,-num) # reduce max to num, then push back
                heapq.heappush(que,-num)
            return res
        return min(helper(nums),helper(nums[::-1]))