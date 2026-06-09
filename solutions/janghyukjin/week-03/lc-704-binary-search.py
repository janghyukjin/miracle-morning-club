from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# ===== Interview Notes =====
# [Binary Search] Easy · Binary Search 기본기
#
# [접근법]
#   1. Closed interval [left, right] — O(log n) / O(1)
#      본인 풀이. 종료조건 `left <= right`, 갱신 `mid ± 1`.
#   2. Half-open [left, right) — O(log n) / O(1)
#      right = len(nums), 종료 `left < right`, 갱신은 left=mid+1 / right=mid.
#      "lower_bound / upper_bound" 류 문제로 확장하기 좋음.
#
# [핵심 아이디어]
#   - "이 구간 안에 답이 있을 수도 있다"는 invariant를 유지하며 반씩 줄인다.
#   - mid 비교 후 *반드시* 범위를 좁혀야 한다 (mid를 양쪽에 모두 남기면 무한루프).
#
# [Follow-up 질문 (면접 단골)]
#   - target이 여러 개면 첫/마지막 위치는? → lower_bound / upper_bound 패턴.
#   - 회전된 정렬 배열이라면? (LC 33) → 두 절반 중 어느 쪽이 정렬됐는지 판별.
#   - 정렬되지 않은 배열에서 "정답 후보가 단조"라면? → 파라메트릭 서치(예: LC 875).
#   - target이 배열에 없을 때 들어갈 위치는? → 종료 시 `left`가 삽입 위치(lower_bound).
#
# [Pitfalls / 흔한 실수]
#   - `mid = (left + right) // 2` 는 파이썬에서는 오버플로 무관하지만, Java/C++에선
#     `left + (right - left) // 2` 가 정석.
#   - 종료조건과 갱신식의 대칭 깨뜨리기 (`<` 와 `mid` / `<=` 와 `mid±1` 짝).
#   - 빈 배열 처리: 본인 풀이는 right=-1로 시작 → 루프 진입 안 함, 안전.
#
# [복잡도]
#   - Time: O(log n)
#   - Space: O(1)
#
# [최적해 (참고) — bisect 한 줄]
#   import bisect
#   def search(nums, target):
#       i = bisect.bisect_left(nums, target)
#       return i if i < len(nums) and nums[i] == target else -1
# ===== End Interview Notes =====
