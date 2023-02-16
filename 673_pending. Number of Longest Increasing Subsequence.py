Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
  
#插牌游戏， 对每一张牌a， 要找到牌堆顶（最小的那种）比a大的最左牌堆， 这是以a结尾的牌能形成lis最长的序列。 放进牌堆， 这个牌堆的顶部就是a。 
#然后再找前一堆牌里比a小的牌 (存的负数， 所以小的牌在末尾）， 从n_path数组里找数量（因为n_path存的是累计和）。 

  

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
    
        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx-1], -num)
                n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]
                
            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0,n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])
              
        return paths[-1][-1]
