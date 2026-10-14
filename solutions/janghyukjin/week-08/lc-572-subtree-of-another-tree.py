from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """탐색(isSubtree) + 검증(isSame) 두 재귀. O(m × n) / O(m)

    바깥 isSubtree는 root의 모든 노드를 후보 시작점으로 훑고, 각 후보에서
    isSame(= LC 100 Same Tree)으로 루트부터 완전히 같은지 검증한다.
    검증 실패는 그 위치만 탈락시킬 뿐 탐색을 끝내지 않으므로 좌우를 or 로 묶는다.
    더 빠르게: 두 트리를 null 표식·구분자 포함 직렬화 후 KMP로 O(m + n).
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r, s) -> bool:
        if r == None and s == None:
            return True
        if r == None or s == None:
            return False
        if r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        return False
