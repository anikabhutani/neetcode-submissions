class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            if hashtable.get(num):
                return True
            hashtable[num] = 1
        return False
        