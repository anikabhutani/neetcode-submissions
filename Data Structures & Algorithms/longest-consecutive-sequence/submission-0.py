class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        maxcount = 0
        for i in nums:
            hashset.add(i)
        for i in nums:
            if i-1 not in hashset:
                j = i
                counter=1
                while j+1 in hashset:
                    counter+=1
                    j+=1
                maxcount = max(maxcount, counter)
        return maxcount