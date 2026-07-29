class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        result = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[i])
            result = max(result, i - left + 1)

        return result
        