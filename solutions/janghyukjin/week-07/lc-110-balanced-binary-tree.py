from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """높이를 리턴하며 balanced flag를 갱신하는 post-order DFS. O(n) / O(h)

    543 Diameter와 같은 뼈대: 각 노드에서 좌우 서브트리 높이를 받아
    차이가 1 초과면 flag를 내리고, 부모에게는 높이 max(left, right) + 1 을
    리턴한다. 노드마다 height()를 따로 부르면 O(n^2)이 되므로
    한 번의 DFS로 높이 계산과 판정을 동시에 한다.
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            nonlocal balanced
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                balanced = False
            return max(left, right) + 1

        dfs(root)
        return balanced
