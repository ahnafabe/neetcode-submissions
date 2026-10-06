class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for index, num in enumerate(nums):
            myMap[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in myMap and myMap[diff] != index:
                return sorted([index, myMap[diff]])
