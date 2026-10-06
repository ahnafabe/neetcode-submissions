class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)): #For every in in nums from 1-4
            if nums[i] == nums[i-1]: 
                return True
        return False
            
