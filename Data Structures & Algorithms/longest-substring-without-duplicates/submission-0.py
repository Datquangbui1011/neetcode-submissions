class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set = set()
        maxSubString = 0
        
        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            
            char_set.add(s[right])
            maxSubString = max(maxSubString, right - left + 1)
            right += 1
        return maxSubString
