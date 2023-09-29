# preorder
# * L R
# [3,9,20,15,7]

# inorder
# L * R
# [9,3,15,20,7]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]

        if not inorder:
            return None

        root_val = preorder.pop(0)  # 3 # 9 # 20 #15 #7
        root = TreeNode(root_val)  # we created a node - 3 # 9 # 20 # 15 #7

        root_index_in_in_order = inorder.index(root_val)  # 1 #0 #1 #0 #0

        left_nodes = inorder[:root_index_in_in_order]  # [9] # [] #[15] #[] #[]
        # [15,20,7] # [] #[7] #[7] #[]
        right_nodes = inorder[root_index_in_in_order+1:]

        root.left = self.buildTree(preorder, left_nodes)
        # preorder = [9,20,15,7] # [] # [15,7] #[7]
        # inorder = [9]          # [] #[15]    #[7]
        root.right = self.buildTree(preorder, right_nodes)
        # preorder = [20,15,7] #[]
        # inorder = [15,20,7]   #[]

        return root


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# [3,9,20,15,7]

# inorder
# L * R
# [9,3,15,20,7]
