class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

        # # Use HashMap
        # hmap = {}

        # for i, x in enumerate(nums):
        #     hmap[x] = i
        
        # for i, x in enumerate(nums):
        #     minus = target - x
        #     if minus in hmap and hmap[minus] != i:
        #         return [i, hmap[minus]]
            
        # return []

        
            
        
