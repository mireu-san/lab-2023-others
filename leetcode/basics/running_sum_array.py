class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         answer = []
#         for i in range(len(nums)):
#             runningSum = 0
#             for j in range(i+1):
#                 runningSum += nums[j]
#             answer.append(runningSum)
#         return answer