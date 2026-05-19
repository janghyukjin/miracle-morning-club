class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set()

        for num in nums:
            sets.add(num)
        
        starters = []

        for num in sets:
            if num-1 in sets:
                continue
            else:
                starters.append(num)
        

        result = []

        for num in starters:
            length = 1
            while True:
                if num + length in sets:
                    length += 1
                else:
                    result.append(length)
                    break
        if len(result) == 0:
            return 0

        return max(result)
