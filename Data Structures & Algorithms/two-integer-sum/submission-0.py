class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(0,len(nums)):
            for num2 in range(num+1,len(nums)):
                if nums[num] + nums[num2] == target:
                    return [num , num2]
        return []
        