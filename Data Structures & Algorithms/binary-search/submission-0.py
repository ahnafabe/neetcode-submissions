class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index
        # else:
        #     return -1
        # above implementation is brute force O(n)

        # try:
        #     index=nums.index(target)
        # except ValueError:
        #     index = -1
        # return index
        # still O(n) as index is a linear search

        l = 0
        r = len(nums) - 1
        mid = (r+l)//2
        while l<=r:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
                mid = (r+l)//2
            elif target > nums[mid]:
                l = mid + 1
                mid = (r+l)//2
        return -1

        
        