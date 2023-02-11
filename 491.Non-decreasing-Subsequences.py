#Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

#Example 1:

#Input: nums = [4,6,7,7]
#Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#Example 2:

#Input: nums = [4,4,3,2,1]
#Output: [[4,4]]

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def rec(prefix, start):
            if len(prefix) >=2: ans.append(prefix[:])
            seen = set()
            for i in range(start, N):
                n = nums[i]
                if n in seen: continue
                if (not prefix) or n >= prefix[-1]:
                    seen.add(n)
                    prefix.append(n)
                    rec(prefix, i+1)
                    prefix.pop()
            return
        rec([], 0)
        return ans