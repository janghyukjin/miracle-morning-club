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