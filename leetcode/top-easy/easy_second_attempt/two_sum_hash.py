class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashTable:
                return [i, hashTable[complement]]
            hashTable[nums[i]] = i