from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """높이를 리턴하며 답을 갱신하는 post-order DFS. O(n) / O(h)

    각 노드를 경로의 꼭대기로 봤을 때 그 노드를 지나는 최장 경로는
    (왼쪽 높이 + 오른쪽 높이) 엣지. 이 값으로 self.res 를 갱신하고,
    부모에게는 경로 길이가 아니라 높이 max(left, right) + 1 을 리턴한다.
    리턴값과 정답이 다른 것이 이 문제의 핵심.
    """

    def dfs(self, head, left_max, right_max):
        if head == None:
            return 0
        left_max = self.dfs(head.left, left_max, right_max)
        right_max = self.dfs(head.right, left_max, right_max)
        self.res = max(self.res, left_max + right_max)

        return max(left_max, right_max) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0, 0)
        return self.res
