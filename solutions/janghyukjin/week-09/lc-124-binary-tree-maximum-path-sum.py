# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """543 Diameter 틀 + 노드 값 합 + 음수 가지 버리기. O(n) / O(h)

    각 노드를 경로의 꼭대기로 보면 그 노드에서 꺾이는 최대 경로 합은
    node.val + left + right. 이 값으로 self.res 를 갱신하고,
    부모에게는 한쪽 가지만 이어 갈 수 있으므로 node.val + max(left, right) 를 리턴한다.
    543 과 다른 점:
      - 엣지 개수(+1)가 아니라 노드 값(+node.val)을 더한다
      - 자식 리턴값이 음수면 그 가지는 안 가는 게 이득 → max(0, dfs(...))
      - 전부 음수일 수 있으므로 res 시작값은 0 이 아니라 root.val (노드 최소 1개 보장)
    """

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val

        dfs(root)
        return self.res
