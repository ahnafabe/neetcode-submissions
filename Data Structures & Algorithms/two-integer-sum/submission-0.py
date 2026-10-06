class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i == j):
                    continue
                elif (nums[i] + nums[j]) == target:
                    solutions.append(i)
                    solutions.append(j)
                    return solutions
                else:
                    continue
        return []
