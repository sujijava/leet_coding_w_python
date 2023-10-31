# preorder
# * L R
# [3,9,20,15,7]

# inorder
# L * R
# [9,3,15,20,7]

class Solution:
    def buildTree(self, preorder, inorder):
        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]

        if not inorder:
            return None

        root_val = preorder.pop(0)  # 3 # 9 # 9
        root = TreeNode(root_val)  # we created a node - 3 # 9

        root_idx_inorder = inorder.index(root_val)  # 1 #0

        left_nodes = inorder[:root_idx_inorder]  # [9] # []
        right_nodes = inorder[root_idx_inorder+1:]  # [15,20,7] # []

        root.left = self.buildTree(preorder, left_nodes)
        # preorder = [9,20,15,7] # []
        # inorder = [9]          # []
        root.right = self.buildTree(preorder, right_nodes)
        # preorder = [9,20,15,7]
        # inorder = [15,20,7]

        return root
