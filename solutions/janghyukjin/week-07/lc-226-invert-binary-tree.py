from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """재귀 DFS — 각 노드에서 좌우 자식을 스왑하고 내려간다. O(n) / O(h)

    스왑 시점(pre-order)이든 내려갔다 온 뒤(post-order)든 결과는 같다.
    모든 노드를 정확히 한 번씩 방문하므로 O(n), 스택 깊이는 트리 높이 h
    (치우친 트리 최악 O(n), 균형 트리 O(log n)).
    """

    def dfs(self, head):
        if head == None:
            return
        head.left, head.right = head.right, head.left
        self.dfs(head.left)
        self.dfs(head.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
