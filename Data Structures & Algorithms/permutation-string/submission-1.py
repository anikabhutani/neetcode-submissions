class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s = sorted(s1)
        while left <= (len(s2) - len(s1)):
            if sorted(s2[left:right]) == s:
                return True
            left += 1
            right += 1

        return False