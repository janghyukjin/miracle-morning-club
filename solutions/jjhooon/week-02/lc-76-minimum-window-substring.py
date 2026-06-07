from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        size = len(count_t)
        check = 0
        left = 0

        # Window
        window = dict()
        window_size = float('inf')
        
        answer = ""

        for i in range(len(s)):
            char = s[i]
            window[char] = window.get(char, 0) + 1
            
            if char in count_t and window[char] == count_t[char]:
                check += 1

            while check == size:
                substring_size = i - left + 1

                if substring_size < window_size:
                    window_size = min(window_size, substring_size)
                    answer = s[left:i+1]
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] < count_t[left_char]:
                    check -= 1

                left += 1
        
        return answer