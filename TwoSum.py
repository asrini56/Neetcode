#1. Two Sum, Time/Space - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            if target - nums[i] in numDict.keys():
                return [numDict[target - nums[i]],i]
            numDict[nums[i]] = i
