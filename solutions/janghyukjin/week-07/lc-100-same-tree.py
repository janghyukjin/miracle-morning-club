from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """두 트리를 동시에 내려가는 재귀. O(min(n, m)) / O(h)

    베이스 케이스(둘 다 None → True, 한쪽만 None → False, 값 다름 → False)를
    함수 첫머리에서 처리하고, 자식은 None 여부를 부모가 미리 따지지 않고
    그대로 재귀로 내려보낸다. 좌우 재귀 결과를 and 로 묶어 리턴 (단락평가로
    왼쪽이 False면 오른쪽은 타지 않음). 572 Subtree에서 서브루틴으로 재사용.
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p != None and q != None:
            if p.val != q.val:
                return False
        elif p == None and q == None:
            return True
        else:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
