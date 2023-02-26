""" You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.
Example 2:

Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.
Example 3:

Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1. """

#hard, # dp = [0] * max(nums)， 前提条件: 最大数比较小
#对每一个数n和idx， 找dp[n-2] 到dp[n-k-1]之间的最大值m， 则dp[idx] = m+1
#用segment tree来找最大值比较快
class Seg:
    def __init__(self, N) -> None:
        self.N = N
        print('N=', N)
        self.tree = [0] * 4 * self.N
    def query(self, rt, l, r, i1, i2):
        
        if l == i1 and r == i2: 
            #print('query:', rt, l, r, i1, i2, '=', self.tree[rt])
            return self.tree[rt]
        if i1 > i2: 
            return 0
        mid = (l+r)//2

        lm = self.query(rt*2+1, l, mid, i1, min(mid, i2))
        rm = self.query(rt*2+2, mid+1, r, max(mid+1, i1), i2)
        
        ret =  max(lm, rm)
        #print('query:', rt, l, r, i1, i2, '=', ret)
        return ret
    def update(self, rt, l, r, i, v):
        
        mid = (l+r) // 2
        if i < l or i > r: return
        if l == r == i: 
            print('tree ', rt, v)
            self.tree[rt] = v
            return
        self.tree[rt] = max(self.tree[rt], v)
        if i > mid:
            self.update(rt*2+2, mid+1, r, i, v)
        else:
            self.update(rt*2+1, l, mid, i, v)
        return

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        # dp = [0] * max(nums)， 前提条件: 最大数比较小
        #对每一个数n和idx， 找dp[n-2] 到dp[n-k-1]之间的最大值m， 则dp[idx] = m+1
        #用segment tree来找最大值比较快
        N = max(nums)
        segtree = Seg(N)
        dp = [0] * N
        ans = 1
        for i, n in enumerate(nums):
            dp[n-1] = max(dp[n-1], segtree.query(0, 0, N-1, max(0, n-k-1), n-2) + 1)
            segtree.update(0, 0, N-1, n-1, dp[n-1])
            ans = max(ans, dp[n-1])
            #print(dp)
        return ans
        
        
        
        N = len(nums)
        dp=[1] * N
        ans = 1
        for i, n in enumerate(nums):
            for j in range(i-1, -1, -1):
                if 0<nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        return ans


sol = Solution()
nums = [4,2,1,4,3,4,5,8,15]
k = 3
sol.lengthOfLIS(nums, k)