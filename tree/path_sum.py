class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        remaining = targetSum - root.val
        
        if not root.left and not root.right:
            return remaining == 0
        
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)