from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """BFS + 층 카운터. O(n) / O(w) (w = 가장 넓은 층의 노드 수, 최악 n/2)

    층이 시작되는 순간 큐에는 정확히 그 층 노드만 있으므로, 그 길이를 length로
    잡아두고 하나 꺼낼 때마다 줄인다. 0이 되면 층 종료 → tmp를 ans에 넣고,
    tmp는 새 리스트로 교체(같은 객체를 다시 쓰면 ans 안 항목까지 바뀜),
    length는 지금 큐 길이(= 다음 층 노드 수)로 갱신.
    표준형은 while 안에 for _ in range(len(queue)) 를 두는 이중 루프.
    """

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
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
                ans.append(tmp)
                length = len(queue)
                tmp = []
        return ans
