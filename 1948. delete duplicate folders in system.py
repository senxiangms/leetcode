""" Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z

However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order. 

Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
Output: [["d"],["d","a"]]
Explanation: The file structure is as shown.
Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
folder named "b".

"""
#用trie 来记录所有排序好的目录
#第一遍遍历递归求signature， (c1 + sig(child[c1]) c2+sig(child[c2])) 并且记录每个sig 对应的node : mem[sig].append(node)
#然后遍历mem， 标记所有节点是否要删除， 注意避免叶子节点， 因为叶子节点的特征都一样
#最后一遍递归遍历trie， 输出未删除节点的path
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.dl = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        def dfs1(node):
            key = "(" + "".join(c + dfs1(node.child[c]) for c in node.child) + ")"
            if key != "()": pattern[key].append(node)
            return key
        
        def dfs2(node, path):
            for c in node.child:
                if not node.child[c].dl:
                    dfs2(node.child[c], path + [c])
            if path: ans.append(path[:])
            
        pattern, root, ans = defaultdict(list), Node(), []
        
        for path in sorted(paths):
            node = root
            for c in path: node = node.child[c]
                
        dfs1(root)
        
        for nodes in pattern.values():
            if len(nodes) > 1:
                for i in nodes: i.dl = True
        
        dfs2(root, [])
        return ans