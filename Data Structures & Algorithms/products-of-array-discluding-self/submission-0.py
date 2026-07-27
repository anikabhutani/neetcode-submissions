class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        result = []
        for i in range(len(nums)):
            left.append(left[-1] * nums[i])
        for i in range(len(nums)):
            right.append(right[-1] * nums[len(nums) - 1 - i])
        for i in range(len(nums)):
            result.append(left[i] * right[len(nums) - i - 1])

        return result