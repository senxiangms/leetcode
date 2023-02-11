""" You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

  """

  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        #Q + N
        #第一遍遍历树改变val到val, left_depth_include_self, right_depth_include_self, 函数返回选择左边时， 选择右边时的层数

        #第二遍遍历记录每一个节点如果被删除， 整体的深度， 所以要carry根的左右深度
        def get_depth(rt, cur): #return layers started from rt
            if rt is None: return [0, 0]
            left = get_depth(rt.left, cur+1)
            right = get_depth(rt.right, cur+1)
            rt.val = [rt.val, cur+max(left), cur+max(right)]
            return [max(left) +1, max(right)+1]
        mp= collections.defaultdict()
        carry = -1
        def gensol(rt, carry, dict):
            if rt.left:
                mp[rt.left.val[0]] = max(carry, rt.val[2])
                gensol(rt.left, max(carry, rt.val[2]), dict)
            if rt.right:
                mp[rt.right.val[0]] = max(carry, rt.val[1])
                gensol(rt.right, max(carry, rt.val[1]), dict)
            return

        get_depth(root, 0)
        gensol(root, -1, mp)
        ans = []
        for q in queries:
            ans.append(mp[q])
        return ans

        get_depth(root, 0)


        
        
        
        #slow Q*N
        def depth(rt, n):
            if rt is None: return -1, False
            if rt.val == n:
                return -1, True
            ld, inleft = depth(rt.left, n)
            rd, inright = depth(rt.right, n)
            
            d = max(ld+1, rd+1)
            return d, inleft or inright
        
        ans = []
        for q in queries:
            d, _ = depth(root, q)
            ans.append(d)
        return ans
