class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(1,len(nums)):
            if nums[num] == nums[num - 1]:          # jasa ki nums[num] == nums[num - 1]
                return True                         # [1] == [0] (checking the index value)
        else : return False
