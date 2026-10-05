# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Plan / Walkthrough:
#
# BST rule:
#   left subtree < node < right subtree
#
# Example:
#       5
#      / \
#     2   7
#        / \
#       6   8
#
# Start with the widest range:
#   -inf < 5 < +inf  => good
#
# Go left:
#   -inf < 2 < 5     => good
#   2 has no children => return True
#
# Go right:
#   5 < 7 < +inf     => good
#
#   Go left from 7:
#       5 < 6 < 7    => good
#
#   Go right from 7:
#       7 < 8 < +inf => good
#
# Every node is within its valid range => BST is valid.
#
# For left subtree:
#   valid(node.left, left, node.val)
#
# For right subtree:
#   valid(node.right, node.val, right)
#
# Both must be valid:
#   valid(node.left, left, node.val)
#   AND
#   valid(node.right, node.val, right)

        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
            


