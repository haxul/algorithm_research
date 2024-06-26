from typing import List, Optional

from neetcode_all_course.leetcode import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: TreeNode):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
