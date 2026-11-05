class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {} #key is number value is index
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in myMap:
                return [myMap[compliment], i]
            myMap[nums[i]] = i