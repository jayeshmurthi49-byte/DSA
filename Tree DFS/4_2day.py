# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:
# https://www.youtube.com/watch?v=d4zLyf32e3I
import collections

def onlyright(root):
    res  = []
    q =  collections.deque([root])
    

    while q:
        rightside  = None
        qlen = len(q)

        for i in range(qlen):
            node  = q.popleft()
            if node:
                rightside = node
                q.append(node.left)
                q.append(node.right)
        if rightside:
            res.append(rightside.val)

    return res
