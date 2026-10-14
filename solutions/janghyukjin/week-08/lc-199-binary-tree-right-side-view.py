from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """102 레벨 순회 + 층의 마지막 값만. O(n) / O(w)

    자식을 왼쪽 → 오른쪽 순으로 넣으므로 한 층의 tmp는 왼→오 순서이고,
    tmp[-1]이 오른쪽에서 보이는 노드. "오른쪽 자식만 따라가기"가 아니라
    "층의 마지막"이라 오른쪽 가지가 짧을 때 왼쪽 가지 노드도 정확히 잡힌다
    (예: [1,2,3,4,null,null,null,5] → [1,3,4,5]).
    더 줄이면 length == 0 순간의 node가 곧 층의 마지막 → tmp 없이 node.val.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        tmp = []
        length = len(queue)
        while queue:
            node = queue.popleft()
            tmp.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            length -= 1
            if length == 0:
                ans.append(tmp[-1])
                length = len(queue)
                tmp = []
        return ans
