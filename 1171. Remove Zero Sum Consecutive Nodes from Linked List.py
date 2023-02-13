""" Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1] """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#node保存前缀和， 以后删除字典entry需要用到
#
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp=collections.defaultdict()

        p = head
        if p is None: return None
        cur_sum = 0
        prev = None
        mp[0] =  None
        while p:
            cur_sum += p.val
            if cur_sum in mp:
                p2 = mp[cur_sum]
                removed = p2.next if p2 else head
                rem_tail = p
                while removed and removed != rem_tail:
                    del mp[removed.psum]
                    removed = removed.next
                    
                if p2:
                    p2.next = p.next
                else:
                    head = p.next
            else:    
                mp[cur_sum] = p
            
            p.psum = cur_sum
            prev = p
            p = p.next

        return head
