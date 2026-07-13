# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Input:  root =    3
#                  / \
#                 4   5
#                / \
#               1   2

#         subRoot = 4
#                  / \
#                 1   2

# Output: True ✅

# Input:  root =    3
#                  / \
#                 4   5
#                / \
#               1   2
#                  /
#                 0

#         subRoot = 4
#                  / \
#                 1   2

# Output: False ❌


def issubtree(root,subtree):
    def issame(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (issame(p.left,q.left) and issame(p.right,q.right))
    
    def dfs(node):
        if not node:
            return False

        if issame(node,subtree):
            return True

        return dfs(node.left) or dfs(node.right)

    return dfs(root)    
