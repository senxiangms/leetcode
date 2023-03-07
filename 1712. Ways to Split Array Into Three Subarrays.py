""" A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
  """

 #对每种可能的第一分割点, 找到第二个分割点的最大right和最小left。 因为first点递增， 所以第二个分割点也不会往左移动。从而复杂度为O(n) right-left即为每个第一分割点时第二分割点的个数
 class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        i = 0
        L = len(nums)
        
        pref_sum = [nums[0]]
        for x in range(1, L):
            pref_sum.append(nums[x]+pref_sum[-1])
        r1 = r2 = 0
        ans = 0
        for i in range(0, L-2):
            while r1 <= i or (r1 < L-1 and pref_sum[r1] < pref_sum[i] * 2):
                r1+=1
            while r2 < r1 or (r2 < L-1 and pref_sum[-1] - pref_sum[r2] >= pref_sum[r2] - pref_sum[i]):
                r2+=1
            ans = (ans + r2-r1)%(10**9+7)
        return ans
