class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # hash table 생성
        for i in range(n):
            numMap[nums[i]] = i

        # target - nums[i]가 hash table에 있는지 확인
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []