""" You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:


Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
  """

#dfs 自底向上贪心， 节点自己有camera的话， 则设为1， 如果自己被叶子cover ， 设为2

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # set the value of camera nodes to 1
        # set the value of monitored parent nodes to 2
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            res = dfs(node.left)+dfs(node.right)
            # find out if current node is a root node / next node in line to be monitored
            curr = min(node.left.val if node.left else float('inf'), node.right.val if node.right else float('inf'))
            if curr == 0:
                # at least one child node requires monitoring, this node must have a camera
                node.val = 1
                res += 1
            elif curr == 1:
                # at least one child node is a camera, this node is already monitored
                node.val = 2
            # if curr == float('inf'), the current node is a leaf node; let the parent node monitor this node
            # if curr == 2, all child nodes are being monitored; treat the current node as a leaf node
            return res
        # ensure that root node is monitored, otherwise, add a camera onto root node
        return dfs(root)+(root.val == 0)