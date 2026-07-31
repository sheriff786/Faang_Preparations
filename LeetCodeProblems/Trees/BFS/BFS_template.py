# Definition for a binary tree node.

'''
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

'''



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        curr_level_nodes =[]
        count=len(queue)
        res=[]

        while len(queue)>0:

            root=queue.popleft()
            curr_level_nodes.append(root.val)
            count=count-1
            
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            if count==0:
                res.append(curr_level_nodes)
                curr_level_nodes=[]
                count=len(queue)
        return res


#N-arrya Tree traversal 

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        queue = []
        current_level_node=[]
       
        queue.append(root)
        count=1
        res=[]

        while len(queue)>0:

            root = queue.pop(0)
            count = count -1
            current_level_node.append(root.val)
            
            for child in root.children:
                queue.append(child)
            # if root.left:
            #     queue.append(root.left)
            # if root.right:
            #     queue.append(root.right)

            if count==0:
                res.append(current_level_node)
                count=len(queue)
                current_level_node=[]

        # res.reverse()     
        return res
#Binary tree current level nodes 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []


        queue = deque()
        queue.append(root)
        count=len(queue)
        res=[]
        current_level_node=[]

        while len(queue)>0:

            root = queue.popleft()
            count = count -1
            current_level_node.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            if count==0:
                size=len(current_level_node)
                res.append(current_level_node[size-1])
                count=len(queue)
                current_level_node=[]
    
        return res
    
    #Binary tree Zig zag traversal
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        queue = []
        current_level_node=[]
       
        queue.append(root)
        count=1
        res=[]

        left=True
        # right=False

        while len(queue)>0:

            root = queue.pop(0)
            count = count -1
            current_level_node.append(root.val)
            
            
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            if count==0:
                if left:
                    res.append(current_level_node)
                    count=len(queue)
                    current_level_node=[]
                    left=False
                else:
                    current_level_node.reverse()
                    res.append(current_level_node)
                    count=len(queue)
                    current_level_node=[]
                    # right=False
                    left=True

                

        # res.reverse()     
        return res
#Binary Tree Zig ZAG

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        queue = []
        current_level_node=[]
       
        queue.append(root)
        count=1
        res=[]

        flag=True
        # right=False

        while len(queue)>0:

            root = queue.pop(0)
            count = count -1
            current_level_node.append(root.val)
            
            
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            if count==0:
                if flag==False:
                    current_level_node.reverse()

                
                res.append(current_level_node)
                count=len(queue)
                current_level_node=[]

                flag=not flag
             
        return res
        