class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in myMap:
                return [myMap[pair], i]
            myMap[nums[i]] = i
        
        