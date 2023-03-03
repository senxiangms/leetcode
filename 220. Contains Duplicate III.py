""" You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false. """

#维护一个前indexDiff 元素的滑动窗口， 记录窗口里每个元素属于哪个bucket （按valdiff大小划分bucket）
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getid(x, w):
            if x < 0:
                x = -x
                id = (x-1)//w+1
                return -id
            else:
                return x//w
        bucket={}
        if k == 0:
            return False
        for i, n in enumerate(nums):
            bid = getid(n, t+1)
            if bid in bucket:
                return True
            if bid-1 in bucket and  n - bucket[bid-1] <=t:
                return True
            if bid+1 in bucket and bucket[bid+1] - n <=t:
                return True
            if i-k  >= 0:
                lbid = getid(nums[i-k], t+1)
                #print('remove i:', i, nums[i-k], lbid)
                del bucket[lbid]
            bucket[bid] = n
        return False