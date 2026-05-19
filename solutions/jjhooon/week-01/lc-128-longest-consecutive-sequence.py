class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0

        starting = []
        for num in nums:
            if num-1 not in nums:
                starting.append(num)

        answer = []
        for start in starting:
            tmp = 1
            
            while start + tmp in nums:
                tmp += 1
            
            answer.append(tmp)
            tmp = 1

        return max(answer) if len(answer) else 0


# ===== Interview Notes =====
# [Longest Consecutive Sequence] Medium · Hash Set
# 제약: O(n) time
#
# [접근법]
#   1. Sort — O(n log n) / O(1)
#      허용되지만 문제 요구 아님
#   2. Hash set (최적) — O(n) / O(n)
#      시퀀스 시작점만 (n-1이 set에 없는 원소)에서 확장
#
# [Follow-up 질문 (면접 단골)]
#   - 시퀀스 자체를 반환하려면?
#   - 스트리밍에서?
#   - Union-Find로 풀 수 있나? (가능, 비효율적)
#
# [Pitfalls / 흔한 실수]
#   - 모든 원소에서 확장하면 O(n²)
#   - 중복 처리
#   - 빈 배열 edge case
#
# [최적해 (참고)]
#   s = set(nums)
#   best = 0
#   for n in s:
#       if n - 1 not in s:  # 시퀀스 시작점
#           cur = n
#           while cur + 1 in s: cur += 1
#           best = max(best, cur - n + 1)
#   return best
# ===== End Interview Notes =====
