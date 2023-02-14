You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.

#split 2N list to first half and second half
#for each half, get C(n, k) combinations, k = 0 ~ N, each c_n_k has a sum, save to dictionary mp[k] =[sum1, sum2, sum3, sum_c_n_k]
#for k1 = 1 ~ N-1 (because when k=0 for first half, include it in ans),  k2 is N-k1
#mp[k1] is a list of sum,  sort mp[k2], for each sum in mp[k1], bisect sorted(mp[k2]) with target-sum  
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2 # Note this is N/2, ie no. of elements required in each.
        #split
        def get_sums(nums): # generate all combinations sum of k elements
            ans = {}
            N = len(nums)
            for k in range(1, N+1): # takes k element for nums
                sums = []
                for comb in combinations(nums, k):
                    s = sum(comb)
                    sums.append(s)
                ans[k] = sums
            return ans
        
        left_part, right_part = nums[:N], nums[N:]
        left_sums, right_sums = get_sums(left_part), get_sums(right_part)
        ans = abs(sum(left_part) - sum(right_part)) # the case when taking all N from left_part for left_ans, and vice versa
        total = sum(nums) 
        half = total // 2 # the best sum required for each, we have to find sum nearest to this
        for k in range(1, N):
            left = left_sums[k] # if taking k no. from left_sums
            right = right_sums[N-k] # then we have to take remaining N-k from right_sums.
            right.sort() # sorting, so that we can binary search the required value
            for x in left:
                r = half - x # required, how much we need to add in x to bring it closer to half.
                p = bisect.bisect_left(right, r) # we are finding index of value closest to r, present in right, using binary search
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff) 
        return ans
      
      
