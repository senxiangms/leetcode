""" 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 """
#p0=0， p2= N-1
#cur = 0
#如果nums[cur]为0， 则把p0 和cur位置的颜色调换， 并且p0和cur 后移 （因为p0原先对应的颜色肯定是0或者1， 所以cur可以后移)
#如果nums[cur]为2， 则把p0和p2位置的颜色调换， p2前移， cur不移动
#总结起来p0指向0的尾巴后一格， p2指向2的头部前一格， p0和cur之间都是1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = p0 = 0
        p2 = len(nums)-1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur+=1
                p0+=1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur+=1
        return