""" You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
Return the number of pairs that satisfy the conditions.

 

Example 1:

Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
Output: 3
Explanation:
There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3. """

#首先找到把两个数组求索引对的问题转变为[nums1[i] - nums2[i] for i ..]数组的满足条件的索引对问题
#其次对每个delta_i， 0~i-1之前元素进入sortedlist， 用二分搜索bisect_right (delta_i+diff) 可以比较快的得到满足条件的个数
from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        #nums1[i]-nums2[i] - (nums1[j]-nums2[j]) <= diff
        N = len(nums1)
        arr = [nums1[i] - nums2[i] for i in range(N)]
        seen = SortedList()
        ans = 0
        print(arr)
        for n in arr:
            
            pos = seen.bisect_right(n+diff)
            ans += pos
            #print(seen, n, pos)
            seen.add(n)
        return ans