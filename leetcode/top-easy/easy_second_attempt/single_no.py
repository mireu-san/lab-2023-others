class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
    

# previous attempt:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hashset = set()
        
#         for i in range(0, len(nums)):
#             if nums[i] in hashset:
#                 hashset.remove(nums[i])
#             else:
#                 hashset.add(nums[i])
#         for j in hashset:
#             return j