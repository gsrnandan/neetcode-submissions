class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            if len(set(nums)) < len(nums):
                return True
        return False