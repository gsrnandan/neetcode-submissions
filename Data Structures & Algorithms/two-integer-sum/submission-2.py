class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        maps = {}
        for i, num in enumerate(nums):
            maps[num] = i                      # value -> index (last occurrence wins)

        for i, num in enumerate(nums):
            complement = target - num
            if complement in maps and maps[complement] != i:
                return [i, maps[complement]]
        return []