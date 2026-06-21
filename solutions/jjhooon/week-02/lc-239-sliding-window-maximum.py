from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        q = deque()
        answer = []

        for i, num in enumerate(nums):
            while q and q[0] <= i-k:
                q.popleft()

            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            if i >= k-1:
                answer.append(nums[q[0]])

        return answer




# 내 처음 풀이
# import heapq

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums or k == 0:
#             return []

#         heap = []
#         answer = []

#         for i in range(k-1):
#             heapq.heappush(heap, (-nums[i], i))

#         for i in range(k-1, len(nums)):
#             heapq.heappush(heap, (-nums[i], i))

#             while heap[0][1] <= i-k:
#                 heapq.heappop(heap)

#             answer.append(-heap[0][0])
            
#         return answer
