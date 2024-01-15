class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val
            
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)
