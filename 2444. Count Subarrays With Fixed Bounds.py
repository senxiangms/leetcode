""" You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
  """

#记录当前元素之前的minKIdx和maxKidx， 如果当前元素不在范围， 左指针设为cur_idx, 如果minKidx和maxKidx都在左指针之后， 则有满足条件的数字。 
#与一般的滑动窗口不一样。 
class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        ans = 0 # initialize answer variable to 0
        j = -1 # initialize starting index of current subarray to -1
        prevMinKIndex = -1 # initialize most recent index of minK to -1
        prevMaxKIndex = -1 # initialize most recent index of maxK to -1

        for i, num in enumerate(nums): # iterate over every element in nums with their index
            if num < minK or num > maxK:
                j = i # if nums[i] is out of range, move starting index of current subarray to i
            if num == minK:
                prevMinKIndex = i # if nums[i] is minK, update most recent index of minK to i
            if num == maxK:
                prevMaxKIndex = i # if nums[i] is maxK, update most recent index of maxK to i

            # calculate number of valid subarrays that end at index i and add to answer
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

        return ans # return the total count of valid subarrays